import os
import requests
import argparse

def add_latest_commit(
    name,
    repoinfo,
    giturl="https://api.github.com/repos/%s/commits",
    date=None,
):
    """Helper function for adding a package versioned at the latest commit to a spack environment.
    The authentication is optional, but note that the api might be rate-limited quite strictly for unauthenticated access.

    :param name: spack name of the package, p.ex: "edm4hep"
    :param repoinfo: description of the owner and repository names, p.ex: "key4hep/edm4hep"
    :param giturl: url that will return a json response with the commit sha when queried with urllib.
       should contain a %s which will be substituted by repoinfo.
       p.ex.: "https://api.github.com/repos/%s/commits"
    """

    headers = {'Accept': 'application/vnd.github+json'}

    github_token = os.environ.get('GITHUB_TOKEN', None)
    if github_token:
        headers += {'Authorization': f'token {github_token}'}

    search_params = {}
    if date:
        search_params = {
            'until': f'{date}',
        }

    response = requests.get(giturl % repoinfo, params=search_params, headers=headers)

    commit = response[0].json()['sha']
    int(commit, 16)

    print(f'  - {name}@{commit}=develop')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Add latest commits to a spack environment")
    parser.add_argument("date", help="date until which to search for commits, for example: 2021-01-01")
    args = parser.parse_args()
    date = args.date

    print()

    add_latest_commit("edm4hep", "key4hep/edm4hep", date)
    add_latest_commit("podio", "aidasoft/podio", date)
    add_latest_commit("dd4hep", "aidasoft/dd4hep", date)
    add_latest_commit("k4fwcore", "key4hep/k4fwcore", date)
    add_latest_commit("k4projecttemplate", "key4hep/k4-project-template", date)
    add_latest_commit("k4simdelphes", "key4hep/k4SimDelphes", date)
    add_latest_commit("k4clue", "key4hep/k4clue", date)
    add_latest_commit("k4gen", "hep-fcc/k4Gen", date)
    add_latest_commit("k4simgeant4", "hep-fcc/k4simgeant4", date)
    add_latest_commit("delphes", "delphes/delphes", date)
    add_latest_commit("fccsw", "hep-fcc/fccsw", date)
    # todo: figure out the api for the cern gitlab instance
    # depends_on('guinea-pig@main')
    # todo: figure out the api for the whizard gitlab instance
    # depends_on('whizard@main +lcio +openloops hepmc=2')
    add_latest_commit("dual-readout", "hep-fcc/dual-readout", date)
    add_latest_commit("fccanalyses", "hep-fcc/fccanalyses", date)
    add_latest_commit("fccdetectors", "hep-fcc/fccdetectors", date)
    add_latest_commit("k4reccalorimeter", "hep-fcc/k4reccalorimeter", date)
    add_latest_commit("cepcsw", "cepc/cepcsw", date)
    add_latest_commit("k4lcioreader", "key4hep/k4LCIOReader", date)
    add_latest_commit("aidatt", "aidasoft/aidatt", date)
    add_latest_commit("cedviewer", "ilcsoft/cedviewer", date)
    add_latest_commit("conformaltracking", "ilcsoft/conformaltracking", date)
    add_latest_commit("clicperformance", "ilcsoft/clicperformance", date)
    add_latest_commit("ced", "ilcsoft/ced", date)
    add_latest_commit("ddkaltest", "ilcsoft/ddkaltest", date)
    add_latest_commit("ddmarlinpandora", "ilcsoft/ddmarlinpandora", date)
    add_latest_commit("fcalclusterer", "fcalsw/fcalclusterer", date)
    add_latest_commit("forwardtracking", "ilcsoft/forwardtracking", date)
    add_latest_commit("k4edm4hep2lcioconv", "key4hep/k4edm4hep2lcioconv", date)
    add_latest_commit("k4marlinwrapper", "key4hep/k4marlinwrapper", date)
    add_latest_commit("gear", "ilcsoft/gear", date)
    add_latest_commit("ilcutil", "ilcsoft/ilcutil", date)
    add_latest_commit("ildperformance", "ilcsoft/ildperformance", date)
    add_latest_commit("kitrackmarlin", "ilcsoft/kitrackmarlin", date)
    add_latest_commit("kaltest", "ilcsoft/kaltest", date)
    add_latest_commit("kitrack", "ilcsoft/kitrack", date)
    add_latest_commit("lcfiplus", "lcfiplus/lcfiplus", date)
    add_latest_commit("lctuple", "ilcsoft/lctuple", date)
    add_latest_commit("lccd", "ilcsoft/lccd", date)
    add_latest_commit("lcio", "ilcsoft/lcio", date)
    add_latest_commit("k4geo", "key4hep/k4geo", date)
    add_latest_commit("marlin", "ilcsoft/marlin", date)
    add_latest_commit("marlinutil", "ilcsoft/marlinutil", date)
    add_latest_commit("marlindd4hep", "ilcsoft/marlindd4hep", date)
    add_latest_commit("marlinreco", "ilcsoft/marlinreco", date)
    add_latest_commit("marlinfastjet", "ilcsoft/marlinfastjet", date)
    add_latest_commit("marlinkinfit", "ilcsoft/marlinkinfit", date)
    add_latest_commit(
        "marlinkinfitprocessors", "ilcsoft/marlinkinfitprocessors"
    )
    add_latest_commit(
        "marlintrkprocessors", "ilcsoft/marlintrkprocessors"
    )
    add_latest_commit("marlintrk", "ilcsoft/marlintrk", date)
    add_latest_commit("overlay", "ilcsoft/overlay", date)
    add_latest_commit("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", date)
    add_latest_commit("physsim", "ilcsoft/physsim", date)
    add_latest_commit("raida", "ilcsoft/raida", date)
    add_latest_commit("sio", "ilcsoft/sio", date)
