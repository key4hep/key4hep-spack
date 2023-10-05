import os
import requests
import argparse


def add_latest_commit(
    name,
    repoinfo,
    # for now supporting only gitlab.cern.ch
    gitlab=False,
    date=None,
):
    """Helper function for adding a package versioned at the latest commit to a spack environment.
    The authentication is optional, but note that the api might be rate-limited for unauthenticated access.

    :param name: spack name of the package, p.ex: "edm4hep"
    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    """

    if not gitlab:
        giturl="https://api.github.com/repos/%s/commits"
    else:
        giturl="https://gitlab.cern.ch/api/v4/projects/%s/repository/commits"

    if gitlab:
        repoinfo = repoinfo.replace("/", "%2F")

    # Apparently this is also fine for gitlab
    headers = {"Accept": "application/vnd.github+json"}

    # gitlab doesn't seem to need a token, maybe there is some rate limiting without one
    token = os.environ.get("GITHUB_TOKEN" if not gitlab else "CERN_GITLAB_TOKEN", None)
    if token:
        headers["Authorization" if not gitlab else "PRIVATE-TOKEN"] = f"token {token}"

    # not tested for gitlab
    search_params = {}
    if date:
        search_params = {
            "until": f"{date}",
        }

    response = requests.get(giturl % repoinfo, params=search_params, headers=headers)

    commit = response.json()[0]['sha' if not gitlab else 'id']
    int(commit, 16)

    print(f"  - {name}@{commit}=develop")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add latest commits to a spack environment"
    )
    parser.add_argument(
        "date", help="date until which to search for commits, for example: 2021-01-01"
    )
    args = parser.parse_args()
    date = args.date

    print()

    add_latest_commit("edm4hep", "key4hep/edm4hep", date=date)
    add_latest_commit("podio", "aidasoft/podio", date=date)
    add_latest_commit("dd4hep", "aidasoft/dd4hep", date=date)
    add_latest_commit("k4fwcore", "key4hep/k4fwcore", date=date)
    add_latest_commit("k4projecttemplate", "key4hep/k4-project-template", date=date)
    add_latest_commit("k4simdelphes", "key4hep/k4SimDelphes", date=date)
    add_latest_commit("k4clue", "key4hep/k4clue", date=date)
    add_latest_commit("k4gen", "hep-fcc/k4Gen", date=date)
    add_latest_commit("k4simgeant4", "hep-fcc/k4simgeant4", date=date)
    add_latest_commit("delphes", "delphes/delphes", date=date)
    add_latest_commit("fccsw", "hep-fcc/fccsw", date=date)
    # todo: figure out the api for the cern gitlab instance
    # depends_on('guinea-pig@main')
    # todo: figure out the api for the whizard gitlab instance
    # depends_on('whizard@main +lcio +openloops hepmc=2')
    add_latest_commit("dual-readout", "hep-fcc/dual-readout", date=date)
    add_latest_commit("fccanalyses", "hep-fcc/fccanalyses", date=date)
    add_latest_commit("fccdetectors", "hep-fcc/fccdetectors", date=date)
    add_latest_commit("k4reccalorimeter", "hep-fcc/k4reccalorimeter", date=date)
    add_latest_commit("cepcsw", "jmcarcell/cepcsw", date=date)
    add_latest_commit("k4lcioreader", "key4hep/k4LCIOReader", date=date)
    add_latest_commit("aidatt", "aidasoft/aidatt", date=date)
    add_latest_commit("cedviewer", "ilcsoft/cedviewer", date=date)
    add_latest_commit("conformaltracking", "ilcsoft/conformaltracking", date=date)
    add_latest_commit("clicperformance", "ilcsoft/clicperformance", date=date)
    add_latest_commit("ced", "ilcsoft/ced", date=date)
    add_latest_commit("ddkaltest", "ilcsoft/ddkaltest", date=date)
    add_latest_commit("ddmarlinpandora", "ilcsoft/ddmarlinpandora", date=date)
    add_latest_commit("fcalclusterer", "fcalsw/fcalclusterer", date=date)
    add_latest_commit("forwardtracking", "ilcsoft/forwardtracking", date=date)
    add_latest_commit("k4edm4hep2lcioconv", "key4hep/k4edm4hep2lcioconv", date=date)
    add_latest_commit("k4marlinwrapper", "key4hep/k4marlinwrapper", date=date)
    add_latest_commit("gear", "ilcsoft/gear", date=date)
    add_latest_commit("ilcutil", "ilcsoft/ilcutil", date=date)
    add_latest_commit("ildperformance", "ilcsoft/ildperformance", date=date)
    add_latest_commit("kitrackmarlin", "ilcsoft/kitrackmarlin", date=date)
    add_latest_commit("kaltest", "ilcsoft/kaltest", date=date)
    add_latest_commit("kitrack", "ilcsoft/kitrack", date=date)
    add_latest_commit("lcfiplus", "lcfiplus/lcfiplus", date=date)
    add_latest_commit("lctuple", "ilcsoft/lctuple", date=date)
    add_latest_commit("lccd", "ilcsoft/lccd", date=date)
    add_latest_commit("lcio", "ilcsoft/lcio", date=date)
    add_latest_commit("k4geo", "key4hep/k4geo", date=date)
    add_latest_commit("marlin", "ilcsoft/marlin", date=date)
    add_latest_commit("marlinutil", "ilcsoft/marlinutil", date=date)
    add_latest_commit("marlindd4hep", "ilcsoft/marlindd4hep", date=date)
    add_latest_commit("marlinreco", "ilcsoft/marlinreco", date=date)
    add_latest_commit("marlinfastjet", "ilcsoft/marlinfastjet", date=date)
    add_latest_commit("marlinkinfit", "ilcsoft/marlinkinfit", date=date)
    add_latest_commit("marlinkinfitprocessors", "ilcsoft/marlinkinfitprocessors")
    add_latest_commit("marlintrkprocessors", "ilcsoft/marlintrkprocessors")
    add_latest_commit("marlintrk", "ilcsoft/marlintrk", date=date)
    add_latest_commit("opendatadetector", "acts/OpenDataDetector", gitlab=True, date=date)
    add_latest_commit("overlay", "ilcsoft/overlay", date=date)
    add_latest_commit("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", date=date)
    add_latest_commit("physsim", "ilcsoft/physsim", date=date)
    add_latest_commit("raida", "ilcsoft/raida", date=date)
    add_latest_commit("sio", "ilcsoft/sio", date=date)
