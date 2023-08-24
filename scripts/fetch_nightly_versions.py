import os


def k4_lookup_latest_commit(repoinfo, giturl):
    """Use a github-like api to fetch the commit hash of the main branch.
    Constructs and runs a command of the form:
    # curl -s -u user:usertoken https://api.github.com/repos/hep-fcc/fccsw/commits/main -H "Accept: application/vnd.github.VERSION.sha"
    The authentication is optional, but note that the api might be rate-limited quite strictly for unauthenticated access.
    The envrionment variables
      GITHUB_USER
      GITHUB_TOKEN
    can be used for authentication.

    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    :type repoinfo: str
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits/main"
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
    curl_command = " ".join(curl_command)
    commit = os.popen(curl_command).read()
    # check that what we got looks like a hash
    int(commit, 16)
    return commit


def k4_add_latest_commit(
    name,
    repoinfo,
    giturl="https://api.github.com/repos/%s/commits/main",
    master=False,
):
    """Helper function for adding a package versioned at the latest commit to a spack environment.

    :param name: spack name of the package, p.ex: "edm4hep"
    :type name: str
    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    :type repoinfo: str
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits/main"
    :type giturl:, str, optional
    """
    if master:
        giturl = giturl.replace("main", "master")
    commit = k4_lookup_latest_commit(repoinfo, giturl)
    print("  - %s@%s=develop" % (name, commit))


if __name__ == "__main__":
    print()

    k4_add_latest_commit("edm4hep", "key4hep/edm4hep")
    k4_add_latest_commit("podio", "aidasoft/podio", master=True)
    k4_add_latest_commit("dd4hep", "aidasoft/dd4hep", master=True)
    k4_add_latest_commit("k4fwcore", "key4hep/k4fwcore")
    k4_add_latest_commit("k4projecttemplate", "key4hep/k4-project-template")
    k4_add_latest_commit("k4simdelphes", "key4hep/k4SimDelphes")
    k4_add_latest_commit("k4clue", "key4hep/k4clue")
    k4_add_latest_commit("k4gen", "hep-fcc/k4Gen")
    k4_add_latest_commit("k4simgeant4", "hep-fcc/k4simgeant4")
    k4_add_latest_commit("delphes", "delphes/delphes", master=True)
    k4_add_latest_commit("fccsw", "hep-fcc/fccsw", master=True)
    # todo: figure out the api for the cern gitlab instance
    # depends_on('guinea-pig@main')
    # todo: figure out the api for the whizard gitlab instance
    # depends_on('whizard@main +lcio +openloops hepmc=2')
    k4_add_latest_commit("dual-readout", "hep-fcc/dual-readout", master=True)
    k4_add_latest_commit("fccanalyses", "hep-fcc/fccanalyses", master=True)
    k4_add_latest_commit("fccdetectors", "hep-fcc/fccdetectors")
    k4_add_latest_commit("k4reccalorimeter", "hep-fcc/k4reccalorimeter")
    k4_add_latest_commit("cepcsw", "cepc/cepcsw", master=True)
    k4_add_latest_commit("k4lcioreader", "key4hep/k4LCIOReader")
    k4_add_latest_commit("aidatt", "aidasoft/aidatt", master=True)
    k4_add_latest_commit("cedviewer", "ilcsoft/cedviewer", master=True)
    k4_add_latest_commit("conformaltracking", "ilcsoft/conformaltracking", master=True)
    k4_add_latest_commit("clicperformance", "ilcsoft/clicperformance", master=True)
    k4_add_latest_commit("ced", "ilcsoft/ced", master=True)
    k4_add_latest_commit("ddkaltest", "ilcsoft/ddkaltest", master=True)
    k4_add_latest_commit("ddmarlinpandora", "ilcsoft/ddmarlinpandora", master=True)
    k4_add_latest_commit("fcalclusterer", "fcalsw/fcalclusterer", master=True)
    k4_add_latest_commit("forwardtracking", "ilcsoft/forwardtracking", master=True)
    k4_add_latest_commit("k4edm4hep2lcioconv", "key4hep/k4edm4hep2lcioconv")
    k4_add_latest_commit("k4marlinwrapper", "key4hep/k4marlinwrapper")
    k4_add_latest_commit("gear", "ilcsoft/gear", master=True)
    k4_add_latest_commit("ilcutil", "ilcsoft/ilcutil", master=True)
    k4_add_latest_commit("ildperformance", "ilcsoft/ildperformance", master=True)
    k4_add_latest_commit("kitrackmarlin", "ilcsoft/kitrackmarlin", master=True)
    k4_add_latest_commit("kaltest", "ilcsoft/kaltest", master=True)
    k4_add_latest_commit("kitrack", "ilcsoft/kitrack", master=True)
    k4_add_latest_commit("lcfiplus", "lcfiplus/lcfiplus", master=True)
    k4_add_latest_commit("lctuple", "ilcsoft/lctuple", master=True)
    k4_add_latest_commit("lccd", "ilcsoft/lccd", master=True)
    k4_add_latest_commit("lcio", "ilcsoft/lcio", master=True)
    k4_add_latest_commit("k4geo", "key4hep/k4geo", master=True)
    k4_add_latest_commit("marlin", "ilcsoft/marlin", master=True)
    k4_add_latest_commit("marlinutil", "ilcsoft/marlinutil", master=True)
    k4_add_latest_commit("marlindd4hep", "ilcsoft/marlindd4hep", master=True)
    k4_add_latest_commit("marlinreco", "ilcsoft/marlinreco", master=True)
    k4_add_latest_commit("marlinfastjet", "ilcsoft/marlinfastjet", master=True)
    k4_add_latest_commit("marlinkinfit", "ilcsoft/marlinkinfit", master=True)
    k4_add_latest_commit(
        "marlinkinfitprocessors", "ilcsoft/marlinkinfitprocessors", master=True
    )
    k4_add_latest_commit(
        "marlintrkprocessors", "ilcsoft/marlintrkprocessors", master=True
    )
    k4_add_latest_commit("marlintrk", "ilcsoft/marlintrk", master=True)
    k4_add_latest_commit("overlay", "ilcsoft/overlay", master=True)
    k4_add_latest_commit("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", master=True)
    k4_add_latest_commit("physsim", "ilcsoft/physsim", master=True)
    k4_add_latest_commit("raida", "ilcsoft/raida", master=True)
    k4_add_latest_commit("sio", "ilcsoft/sio", master=True)
