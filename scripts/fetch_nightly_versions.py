import os

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
      #try:
      commit = k4_lookup_latest_commit(repoinfo, giturl)
      #print('  %s: ' % name)
      #print('    version: [commit.%s]' % commit)
      print('    - %s@commit.%s' % (name, commit))

      #depends_on(name + "@commit." + str(commit) + " " + variants, when=when)
      #except:
      #  print("Warning: could not fetch latest commit for " + name)




if __name__ == "__main__":
    print('  specs:')
    k4_add_latest_commit_as_dependency("edm4hep", "key4hep/edm4hep", when="@master")
    k4_add_latest_commit_as_dependency("podio", "aidasoft/podio", when="@master")
    k4_add_latest_commit_as_dependency("dd4hep", "aidasoft/dd4hep", when="@master")
    k4_add_latest_commit_as_dependency("k4fwcore", "key4hep/k4fwcore", when="@master")
    k4_add_latest_commit_as_dependency("k4projecttemplate", "key4hep/k4-project-template", when="@master")

    k4_add_latest_commit_as_dependency("k4simdelphes", "key4hep/k4SimDelphes", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    # needs to fix tests
    #k4_add_latest_commit_as_dependency("k4clue", "key4hep/k4clue", when="@master",
		#		 giturl="https://api.github.com/repos/%s/commits/main")

    k4_add_latest_commit_as_dependency("k4gen", "hep-fcc/k4Gen", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    k4_add_latest_commit_as_dependency("k4simgeant4", "hep-fcc/k4simgeant4", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")
    # todo: figure out the api for the whizard gitlab instance
    # todo: figure out the api for the cern gitlab instance
    k4_add_latest_commit_as_dependency("delphes", "delphes/delphes", when="@master")

    k4_add_latest_commit_as_dependency("fccsw", "hep-fcc/fccsw", when="@master")
    #depends_on('guinea-pig@master', when="@master")
    #depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")


    k4_add_latest_commit_as_dependency("dual-readout", "hep-fcc/dual-readout", when="@master")

    k4_add_latest_commit_as_dependency("fccanalyses", "hep-fcc/fccanalyses", when="@master")


    k4_add_latest_commit_as_dependency("fccdetectors", "hep-fcc/fccdetectors", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    k4_add_latest_commit_as_dependency("k4reccalorimeter", "hep-fcc/k4reccalorimeter", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    k4_add_latest_commit_as_dependency("cepcsw", "cepc/cepcsw", when="@master")



    k4_add_latest_commit_as_dependency("k4lcioreader", "key4hep/k4LCIOReader", when="@master")


    k4_add_latest_commit_as_dependency("aidatt", "aidasoft/aidatt", when="@master")

    k4_add_latest_commit_as_dependency("cedviewer", "ilcsoft/cedviewer", when="@master")

    k4_add_latest_commit_as_dependency("conformaltracking", "ilcsoft/conformaltracking", when="@master")

    k4_add_latest_commit_as_dependency("clicperformance", "ilcsoft/clicperformance", when="@master")

    k4_add_latest_commit_as_dependency("clupatra", "ilcsoft/clupatra", when="@master")

    k4_add_latest_commit_as_dependency("ced", "ilcsoft/ced", when="@master")

    k4_add_latest_commit_as_dependency("ddkaltest", "ilcsoft/ddkaltest", when="@master")

    k4_add_latest_commit_as_dependency("ddmarlinpandora", "ilcsoft/ddmarlinpandora", when="@master")

    k4_add_latest_commit_as_dependency("fcalclusterer", "fcalsw/fcalclusterer", when="@master")

    k4_add_latest_commit_as_dependency("forwardtracking", "ilcsoft/forwardtracking", when="@master")

    k4_add_latest_commit_as_dependency("garlic", "ilcsoft/garlic", when="@master")

    k4_add_latest_commit_as_dependency("k4marlinwrapper", "key4hep/k4marlinwrapper", when="@master")

    k4_add_latest_commit_as_dependency("generalbrokenlines", "GeneralBrokenLines/GeneralBrokenLines", when="@master")

    k4_add_latest_commit_as_dependency("gear", "ilcsoft/gear", when="@master")

    k4_add_latest_commit_as_dependency("ilcutil", "ilcsoft/ilcutil", when="@master")

    k4_add_latest_commit_as_dependency("ildperformance", "ilcsoft/ildperformance", when="@master")

    k4_add_latest_commit_as_dependency("kaldet", "ilcsoft/kaldet", when="@master")

    k4_add_latest_commit_as_dependency("kitrackmarlin", "ilcsoft/kitrackmarlin", when="@master")

    k4_add_latest_commit_as_dependency("kaltest", "ilcsoft/kaltest", when="@master")

    k4_add_latest_commit_as_dependency("kitrack", "ilcsoft/kitrack", when="@master")

    k4_add_latest_commit_as_dependency("lcfiplus", "lcfiplus/lcfiplus", when="@master")

    k4_add_latest_commit_as_dependency("lctuple", "ilcsoft/lctuple", when="@master")

    k4_add_latest_commit_as_dependency("lcfivertex", "ilcsoft/lcfivertex", when="@master")

    k4_add_latest_commit_as_dependency("lich", "danerdaner/lich", when="@master")

    k4_add_latest_commit_as_dependency("lccd", "ilcsoft/lccd", when="@master")

    k4_add_latest_commit_as_dependency("lcio", "ilcsoft/lcio", when="@master")

    k4_add_latest_commit_as_dependency("lcgeo", "ilcsoft/lcgeo", when="@master")

    k4_add_latest_commit_as_dependency("marlin", "ilcsoft/marlin", when="@master")

    k4_add_latest_commit_as_dependency("marlinutil", "ilcsoft/marlinutil", when="@master")

    #k4_add_latest_commit_as_dependency("marlinpandora", "pandorapfa/marlinpandora", when="@master")

    k4_add_latest_commit_as_dependency("marlindd4hep", "ilcsoft/marlindd4hep", when="@master")

    k4_add_latest_commit_as_dependency("marlinreco", "ilcsoft/marlinreco", when="@master")

    k4_add_latest_commit_as_dependency("marlinfastjet", "ilcsoft/marlinfastjet", when="@master")

    k4_add_latest_commit_as_dependency("marlinkinfit", "ilcsoft/marlinkinfit", when="@master")

    k4_add_latest_commit_as_dependency('marlinkinfitprocessors', 'ilcsoft/marlinkinfitprocessors', when='@master')

    k4_add_latest_commit_as_dependency("marlintrkprocessors", "ilcsoft/marlintrkprocessors", when="@master")

    k4_add_latest_commit_as_dependency("marlintrk", "ilcsoft/marlintrk", when="@master")

    k4_add_latest_commit_as_dependency("overlay", "ilcsoft/overlay", when="@master")

    k4_add_latest_commit_as_dependency("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", when="@master")

    #k4_add_latest_commit_as_dependency("pandorapfa", "pandorapfa/pandorapfa", when="@master")


    k4_add_latest_commit_as_dependency("physsim", "ilcsoft/physsim", when="@master")

    k4_add_latest_commit_as_dependency("raida", "ilcsoft/raida", when="@master")

    k4_add_latest_commit_as_dependency("sio", "ilcsoft/sio", when="@master")
