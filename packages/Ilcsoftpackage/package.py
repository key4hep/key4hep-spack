# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

import os

import spack.cmd
import llnl.util.tty as tty
import spack.cmd.common.arguments as arguments
import spack.environment as ev
import spack.util.environment
from  spack.util.environment import *
import spack.user_environment as uenv
import spack.store
import os

from spack.package import PackageBase





def k4_generate_setup_script(env_mod, shell='sh'):
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
            env_set_not_prepend[name] = env_set_not_prepend[name] or isinstance(x, (SetPath, SetEnv))
            # set a dictionary with the environment variables
            x.execute(new_env)
        if env_set_not_prepend[name] and len(actions) > 1:
            tty.warn("Var " + name + "is set multiple times!" )
  
    # deduplicate paths
    for name in  new_env:
      path_list = new_env[name].split(":")
      pruned_path_list = prune_duplicate_paths(path_list)
      new_env[name] = ":".join(pruned_path_list) 


    # fourth, get shell commands
    k4_shell_set_strings = {
        'sh': 'export {0}={1};\n',
    }
    k4_shell_prepend_strings = {
        'sh': 'export {0}={1}:${0};\n',
    }
    cmds = []
    for name in set(new_env):
        if env_set_not_prepend[name]:
            cmds += [k4_shell_set_strings[shell].format(
                name, cmd_quote(new_env[name]))]
        else:
            cmds += [k4_shell_prepend_strings[shell].format(
                name, cmd_quote(new_env[name]))]
    return ''.join(cmds)

def k4_lookup_latest_commit(repoinfo, giturl):
    """Use a github-like api to fetch the commit hash of the master branch.
    Constructs and runs a command of the form:
    # curl -s -u user:usertoken https://api.github.com/repos/hep-fcc/fccsw/commits/master -H "Accept: application/vnd.github.VERSION.sha"
    The authentication is optional, but note that the api might be rate-limited quite strictly for unauthenticated access.
    The envrionment variables 
      GITHUB_USER
      GITHUB_TOKEN
    can be used for authentication.

    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    :type repoinfo: str
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits/master"
    :return: The commit sha of the latest commit for the repo.
    :rtype: str
      
    """
    curl_command = ["curl -s "]
    github_user = os.environ.get("GITHUB_USER", "")
    github_token = os.environ.get("GITHUB_TOKEN", "")
    if github_user and github_token:
      curl_command += [" -u %s:%s " % (github_user, github_token)]
    final_giturl = giturl % repoinfo
    curl_command += [final_giturl]
    curl_command += [' -H "Accept: application/vnd.github.VERSION.sha" ']
    curl_command = ' '.join(curl_command)
    commit = os.popen(curl_command).read()
    test = int(commit, 16)
    return commit

def k4_add_latest_commit_as_dependency(name, repoinfo, giturl="https://api.github.com/repos/%s/commits/master", variants="", when="@master"):
    """ Helper function that adds a 'depends_on' with the latest commit to a spack recipe.

    :param name: spack name of the package, p.ex: "edm4hep"
    :type name: str
    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    :type repoinfo: str
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits/master"
    :type giturl:, str, optional
    :param variants: argument that will be forwarded to depends_on
      example: "+lcio"
    :type variants: str, optional
    :param when: argument that will be forwarded to depends_on
      example: "@master"
    :type when: str, optional
    """
    github_user = os.environ.get("GITHUB_USER", "")
    github_token = os.environ.get("GITHUB_TOKEN", "")
    if github_user and github_token:
      try:
        commit = k4_lookup_latest_commit(repoinfo, giturl)
        depends_on(name + "@commit." + str(commit) + " " + variants, when=when)
      except:
        print("Warning: could not fetch latest commit for " + name)

def k4_add_latest_commit_as_version(git_url, git_api_url="https://api.github.com/repos/%s/commits/master"):
    """ Helper function that adds a 'version' with the latest commit to a spack recipe.
    Note that the 'commit' part of the version is needed to ensure that version comparisons in spack will judge this as the newest version.


    :param git_url: url of a git repository. Needs to end in .git.
      example: "https://github.com/HSF/prmon.git"
    :type git_url: str
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits/master"
    :type giturl: str, optional
    """
    pass



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
    base_url = self.url.rsplit('/', 1)[0]
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
        version_str = 'v%02d-%02d.tar.gz' % (major, minor)
    else:
        version_str = 'v%02d-%02d-%02d.tar.gz' % (major, minor, patch)
    return base_url + '/' + version_str

class Key4hepPackage(PackageBase):

    tags = ['hep', 'key4hep']

class Ilcsoftpackage(Key4hepPackage):
    """This class needs to be present to allow spack to import this file.
    the above function could also be a member here, but there is an
    issue with the logging of packages that use custom base classes.
    """


    
    def url_for_version(self, version):
        return ilc_url_for_version(self, version)

