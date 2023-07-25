"""
Common methods for use in Key4hep recipes
"""

from spack import *
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

try:
    # https://github.com/spack/spack/pull/38944 renamed store -> STORE
    from spack.store import STORE
except ImportError:
    from spack import store as STORE

# TODO: can be removed when spack versions prior to v0.18.1 are no longer needed
try:
    from spack.package import PackageBase
except ImportError:
    from spack.package_base import PackageBase

from shlex import quote as cmd_quote


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
        env_set_not_prepend[name] = False
        for x in actions:
            env_set_not_prepend[name] = env_set_not_prepend[name] or isinstance(
                x, (SetPath, SetEnv)
            )
            # set a dictionary with the environment variables
            x.execute(new_env)
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
    return "".join(cmds)


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
    else:
        version_str = "v%02d-%02d-%02d.tar.gz" % (major, minor, patch)
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
        for dep in spec.traverse(order="post"):
            env_mod.extend(uenv.environment_modifications_for_spec(dep))
            env_mod.prepend_path(uenv.spack_loaded_hashes_var, dep.dag_hash())

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
        # optionally add a symlink (location configurable via environment variable
        try:
            symlink_path = os.environ.get(env_var, "")
            tty.debug("Trying to symlink setup script to: {}".format(env_var))
            if symlink_path:
                # make sure that the path exists, create if not
                if not os.path.exists(os.path.dirname(symlink_path)):
                    os.makedirs(os.path.dirname(symlink_path))
                # make sure that an existing file will be overwritten,
                # even if it is a symlink (for which 'exists' is false!)
                if os.path.exists(symlink_path) or os.path.islink(symlink_path):
                    os.remove(symlink_path)
                os.symlink(os.path.join(prefix, "setup.sh"), symlink_path)
        except:
            tty.warn("Could not create symlink")


class Key4hepPackage(PackageBase):
    tags = ["hep", "key4hep"]


class Ilcsoftpackage(Key4hepPackage):
    """This class needs to be present to allow spack to import this file.
    the above function could also be a member here, but there is an
    issue with the logging of packages that use custom base classes.
    """

    def url_for_version(self, version):
        return ilc_url_for_version(self, version)
