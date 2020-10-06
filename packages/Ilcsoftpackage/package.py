# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

from urllib.request import urlopen
import json


def k4_lookup_latest_commit(name, repoinfo, giturl):
      """
      Use a github-like api to fetch the commit hash of the master branch.

      Parameters:

      name: string
        spack name of the package, p.ex: "edm4hep"
      repoinfo: string
         description of the owner and repository names, p.ex: "key4hep/edm4hep"
      giturl: string
         url that will return a json response with the commit sha when queried with urllib.
         should contain a %s which will be substituted by repoinfo.
         p.ex.: "https://api.github.com/repos/%s/commits/master"
        
      """
      # todo: change to only fetch sha
      # (need to create a request object for this)
      with urlopen(giturl % repoinfo) as response: 
        json_response = json.loads(response.read())
        commit = json_response["sha"]
      return commit

def k4_add_latest_commit_as_dependency(name, repoinfo, giturl="https://api.github.com/repos/%s/commits/master", when="@master"):
      """
      Helper function that adds a 'depends_on' with the latest commit to a spack recipe.

      Parameters:


      name: string
        spack name of the package, p.ex: "edm4hep"
      repoinfo: string
         description of the owner and repository names, p.ex: "key4hep/edm4hep"
      giturl: string, optional
         url that will return a json response with the commit sha when queried with urllib.
         should contain a %s which will be substituted by repoinfo.
         p.ex.: "https://api.github.com/repos/%s/commits/master"
      when: string, optional
        argument that will be forwarded to depends_on
        example: "@master"
      """
      try:
        commit = k4_lookup_latest_commit(name, repoinfo, giturl)
        depends_on(name + "@develop-" + str(commit), when=when)
      except:
        print("Warning: could not fetch latest commit for " + name)

def k4_add_latest_commit_as_version(name, repoinfo, giturl="https://api.github.com/repos/%s/commits/master"):
      """
      Helper function that adds a 'version' with the latest commit to a spack recipe.

      Note that the 'develop' part of the version is needed to ensure that version comparisons in spack will judge this as the newest version.

      Parameters:


      name: string
        spack name of the package, p.ex: "edm4hep"
      repoinfo: string
         description of the owner and repository names, p.ex: "key4hep/edm4hep"
      giturl: string, optional
         url that will return a json response with the commit sha when queried with urllib.
         should contain a %s which will be substituted by repoinfo.
         p.ex.: "https://api.github.com/repos/%s/commits/master"
      """
      try:
        commit = k4_lookup_latest_commit(name, repoinfo, giturl)
        version("develop-"+str(commit), commit=commit, preferred=False)
      except:
        print("Warning: could not fetch latest commit for " + name)


def ilc_url_for_version(self, version):
        # translate version numbers to ilcsoft conventions.
        # in spack, the convention is: 0.1 (or 0.1.0) 0.1.1, 0.2, 0.2.1 ...
        # in ilcsoft, releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        base_url = self.url.rsplit('/', 1)[0]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        # handle the different cases for the patch version:
        # first case, no patch version is given in spack, i.e 0.1
        if len(version) == 2:
            url = base_url + "/v%s-%s.tar.gz" % (major, minor)
        # a patch version is specified in spack, i.e. 0.1.x ...
        elif len(version) == 3:
            patch = str(version[2]).zfill(2)
            # ... but it is zero, and not part of the ilc release url
            if version[2] == 0:
                url = base_url + "/v%s-%s.tar.gz" % (major, minor)
            # ... if it is non-zero, it is part  of the release url
            else:
                url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        else:
            print('Error - Wrong version format provided')
            return
        return url

class Ilcsoftpackage(Package):
    # needs to be present to allow spack to import this file.
    # the above function could also be a member here, but there is an
    # issue with the logging of packages that use custom base classes.
    pass

