"""
Common methods for use in Key4hep recipes
"""

from spack.package import *
from spack.directives import *
from spack.user_environment import *

import os

import spack.cmd
import llnl.util.tty as tty
import spack.platforms
import spack.spec
import spack.util.environment
from spack.util.environment import *
import spack.user_environment as uenv

from spack.store import STORE
from spack.package_base import PackageBase

from shlex import quote as cmd_quote

# List of env variables that will NOT be set
IGNORE_VARS = set(
    [
        # Fix CMP0144 warnings: https://github.com/key4hep/key4hep-spack/issues/525
        "BOOST_ROOT",
        "SPACK_LOADED_HASHES",
        # this fixes loading the local emacs: https://github.com/key4hep/key4hep-spack/issues/486
        "XDG_DATA_DIRS",
    ]
)


def k4_setup_env_for_framework_tests(spec, env):
    """Setup for tests that need the run environment."""
    runenv = environment_modifications_for_spec(spec)
    env.extend(runenv)
    for dspec in spec.traverse(root=False, order="post"):
        dspec.package.setup_run_environment(env)
        # make sure that ROOT_INCLUDE_PATH is set
        if dspec.satisfies("^root"):
            spec["root"].package.setup_dependent_run_environment(env, dspec)


def k4_generate_setup_script(env_mod, shell="sh"):
    """Return shell code corresponding to a EnvironmentModifications object.
    Contrary to the spack environment_modifications() method, this does not evaluate
    the current environment, but generates shell code like:
    export PATH=/new/path:$PATH
    instead of:
    export PATH=/new/path:/current/contents/of/PATH;
    if `/new/path` is to be prepended.

    :param env_mod: spack EnvironmentModifications object
    :type env_mod: class: `spack.EnvironmentModifications`
    :param str shell: type of the shell. Only 'sh' possible at the moment
    :return: Shell code corresponding to the environment modifications.
    :rtype: str
    """
    modifications = env_mod.group_by_name()
    new_env = {}
    # keep track wether this variable is supposed to be a list of paths, or set to a single value
    env_set_not_prepend = {}
    for name, actions in sorted(modifications.items()):
        if name in IGNORE_VARS:
            continue
        env_set_not_prepend[name] = False
        for x in actions:
            env_set_not_prepend[name] = env_set_not_prepend[name] or isinstance(
                x, (SetPath, SetEnv)
            )
            # set a dictionary with the environment variables
            try:
                x.execute(new_env)
            except TypeError:
                tty.warn(f"Could not execute {x} for {name}")
        if env_set_not_prepend[name] and len(actions) > 1:
            tty.warn(f"Var {name} is set multiple times!")

    # deduplicate paths
    for name in new_env:
        path_list = new_env[name].split(":")
        pruned_path_list = prune_duplicate_paths(path_list)
        new_env[name] = ":".join(pruned_path_list)

    # get shell commands
    k4_shell_set_strings = {
        "sh": "export {0}={1}\n",
    }
    k4_shell_prepend_strings = {
        "sh": "export {0}={1}:${0}\n",
    }
    cmds = []
    for name in set(new_env):
        if env_set_not_prepend[name]:
            cmds += [k4_shell_set_strings[shell].format(name, cmd_quote(new_env[name]))]
        else:
            cmds += [
                k4_shell_prepend_strings[shell].format(name, cmd_quote(new_env[name]))
            ]
    return "".join(sorted(cmds))


def ilc_url_for_version(self, version):
    """Translate version numbers to ilcsoft conventions.
    in spack, the convention is: 0.1 (or 0.1.0) 0.1.1, 0.2, 0.2.1 ...
    in ilcsoft, releases are dashed and padded with a leading zero
    the patch version is omitted when 0
    so for example v01-12-01, v01-12 ...

    :param self: spack package class that has a url
    :type self: class: `spack.PackageBase`
    :param version: version
    :type param: str
    """
    base_url = self.url.rsplit("/", 1)[0]
    if len(version) == 1:
        major = version[0]
        minor, patch = 0, 0
    elif len(version) == 2:
        major, minor = version
        patch = 0
    else:
        major, minor, patch = version
    # By now the data is normalized enough to handle it easily depending
    # on the value of the patch version
    if patch == 0:
        version_str = "v%02d-%02d.tar.gz" % (major, minor)
    elif isinstance(patch, int):
        version_str = "v%02d-%02d-%02d.tar.gz" % (major, minor, patch)
    else:  # allow for v00-04-pre
        version_str = "v%02d-%02d-%s.tar.gz" % (major, minor, patch)
    return base_url + "/" + version_str


def install_setup_script(self, spec, prefix, env_var):
    """Create a bash setup script that includes all the dependent packages while
    respecting the PATH variable of the user"""
    # get all dependency specs, including compiler
    # record all changes to the environment by packages in the stack
    env_mod = spack.util.environment.EnvironmentModifications()

    # first setup compiler, similar to build_environment.py in spack
    env_mod.prepend_path("PATH", os.path.dirname(self.compiler.cxx))

    # now walk over the dependencies
    with STORE.db.read_transaction():
        # Between spack 0.20.2 and the next release environment_modifications_for_spec
        # was renamed to environment_modifications_for_specs
        try:
            env_mod.extend(uenv.environment_modifications_for_spec(spec))
        except AttributeError:
            env_mod.extend(uenv.environment_modifications_for_specs(spec))
        env_mod.prepend_path(uenv.spack_loaded_hashes_var, spec.dag_hash())

    if self.compiler.cc:
        env_mod.set("CC", self.compiler.cc)
    if self.compiler.cxx:
        env_mod.set("CXX", self.compiler.cxx)
    if self.compiler.f77:
        env_mod.set("F77", self.compiler.f77)
    if self.compiler.fc:
        env_mod.set("FC", self.compiler.fc)

    # transform to bash commands, and write to file
    cmds = k4_generate_setup_script(env_mod)
    with open(os.path.join(prefix, "setup.sh"), "w") as f:
        f.write(cmds)

    # Try to create a symlink to fjcontrib/include/fastjet/contrib in fastjet/include/fastjet/
    # See https://github.com/key4hep/key4hep-spack/issues/690
    if "fjcontrib" in spec:
        try:
            os.symlink(
                os.path.join(spec["fjcontrib"].prefix, "include", "fastjet", "contrib"),
                os.path.join(spec["fastjet"].prefix, "include", "fastjet", "contrib"),
            )
        except FileExistsError:
            pass


class Key4hepPackage(PackageBase):
    tags = ["hep", "key4hep"]


class Ilcsoftpackage(Key4hepPackage):
    """This class needs to be present to allow spack to import this file.
    the above function could also be a member here, but there is an
    issue with the logging of packages that use custom base classes.
    """

    def url_for_version(self, version):
        return ilc_url_for_version(self, version)
