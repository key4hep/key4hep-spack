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
    # request only the necessary information (commit hash)
    curl_command += [' -H "Accept: application/vnd.github.VERSION.sha" ']
    curl_command = ' '.join(curl_command)
    commit = os.popen(curl_command).read()
    # check that what we got looks like a hash
    test = int(commit, 16)
    return commit

def k4_add_latest_commit(name, repoinfo, giturl="https://api.github.com/repos/%s/commits/master", variants=""):
    """ Helper function for adding a package versioned at the latest commit to a spack environment.

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
    """
    github_user = os.environ.get("GITHUB_USER", "")
    github_token = os.environ.get("GITHUB_TOKEN", "")
    commit = k4_lookup_latest_commit(repoinfo, giturl)
    print('  - %s@%s=develop' % (name, commit))


if __name__ == "__main__":
    print()

    k4_add_latest_commit("edm4hep", "key4hep/edm4hep")
    # k4_add_latest_commit("podio", "aidasoft/podio")
    # k4_add_latest_commit("dd4hep", "aidasoft/dd4hep")
    k4_add_latest_commit("k4fwcore", "key4hep/k4fwcore")
    k4_add_latest_commit("k4projecttemplate", "key4hep/k4-project-template")
    k4_add_latest_commit("k4simdelphes", "key4hep/k4SimDelphes",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("k4clue", "key4hep/k4clue",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("k4gen", "hep-fcc/k4Gen",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("k4simgeant4", "hep-fcc/k4simgeant4",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("delphes", "delphes/delphes")
    k4_add_latest_commit("fccsw", "hep-fcc/fccsw")
    # todo: figure out the api for the cern gitlab instance
    # depends_on('guinea-pig@master')
    # todo: figure out the api for the whizard gitlab instance
    # depends_on('whizard@master +lcio +openloops hepmc=2')
    k4_add_latest_commit("dual-readout", "hep-fcc/dual-readout")
    k4_add_latest_commit("fccanalyses", "hep-fcc/fccanalyses")
    k4_add_latest_commit("fccdetectors", "hep-fcc/fccdetectors",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("k4reccalorimeter", "hep-fcc/k4reccalorimeter",
                         giturl="https://api.github.com/repos/%s/commits/main")
    k4_add_latest_commit("cepcsw", "cepc/cepcsw")
    k4_add_latest_commit("k4lcioreader", "key4hep/k4LCIOReader")
    k4_add_latest_commit("aidatt", "aidasoft/aidatt")
    k4_add_latest_commit("cedviewer", "ilcsoft/cedviewer")
    k4_add_latest_commit("conformaltracking", "ilcsoft/conformaltracking")
    k4_add_latest_commit("clicperformance", "ilcsoft/clicperformance")
    k4_add_latest_commit("clupatra", "ilcsoft/clupatra")
    k4_add_latest_commit("ced", "ilcsoft/ced")
    k4_add_latest_commit("ddkaltest", "ilcsoft/ddkaltest")
    k4_add_latest_commit("ddmarlinpandora", "ilcsoft/ddmarlinpandora")
    k4_add_latest_commit("fcalclusterer", "fcalsw/fcalclusterer")
    k4_add_latest_commit("forwardtracking", "ilcsoft/forwardtracking")
    k4_add_latest_commit("garlic", "ilcsoft/garlic")
    k4_add_latest_commit('k4edm4hep2lcioconv', 'key4hep/k4edm4hep2lcioconv')
    k4_add_latest_commit("k4marlinwrapper", "key4hep/k4marlinwrapper")
    k4_add_latest_commit("generalbrokenlines", "GeneralBrokenLines/GeneralBrokenLines")
    k4_add_latest_commit("gear", "ilcsoft/gear")
    k4_add_latest_commit("ilcutil", "ilcsoft/ilcutil")
    k4_add_latest_commit("ildperformance", "ilcsoft/ildperformance")
    k4_add_latest_commit("kaldet", "ilcsoft/kaldet")
    k4_add_latest_commit("kitrackmarlin", "ilcsoft/kitrackmarlin")
    k4_add_latest_commit("kaltest", "ilcsoft/kaltest")
    k4_add_latest_commit("kitrack", "ilcsoft/kitrack")
    k4_add_latest_commit("lcfiplus", "lcfiplus/lcfiplus")
    k4_add_latest_commit("lctuple", "ilcsoft/lctuple")
    k4_add_latest_commit("lcfivertex", "ilcsoft/lcfivertex")
    k4_add_latest_commit("lich", "danerdaner/lich")
    k4_add_latest_commit("lccd", "ilcsoft/lccd")
    k4_add_latest_commit("lcio", "ilcsoft/lcio")
    k4_add_latest_commit("lcgeo", "key4hep/k4geo")
    k4_add_latest_commit("marlin", "ilcsoft/marlin")
    k4_add_latest_commit("marlinutil", "ilcsoft/marlinutil")
    k4_add_latest_commit("marlindd4hep", "ilcsoft/marlindd4hep")
    k4_add_latest_commit("marlinreco", "ilcsoft/marlinreco")
    k4_add_latest_commit("marlinfastjet", "ilcsoft/marlinfastjet")
    k4_add_latest_commit("marlinkinfit", "ilcsoft/marlinkinfit")
    k4_add_latest_commit('marlinkinfitprocessors', 'ilcsoft/marlinkinfitprocessors')
    k4_add_latest_commit("marlintrkprocessors", "ilcsoft/marlintrkprocessors")
    k4_add_latest_commit("marlintrk", "ilcsoft/marlintrk")
    k4_add_latest_commit("overlay", "ilcsoft/overlay")
    k4_add_latest_commit("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis")
    k4_add_latest_commit("physsim", "ilcsoft/physsim")
    k4_add_latest_commit("raida", "ilcsoft/raida")
    k4_add_latest_commit("sio", "ilcsoft/sio")
