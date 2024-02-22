import os
import requests
import argparse
import yaml


def get_latest_commit(
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
        giturl = "https://api.github.com/repos/%s/commits"
    else:
        giturl = "https://gitlab.cern.ch/api/v4/projects/%s/repository/commits"

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

    commit = response.json()[0]["sha" if not gitlab else "id"]
    int(commit, 16)

    return commit


def get_default_branch(
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
        giturl = "https://api.github.com/repos/%s"
    else:
        giturl = "https://gitlab.cern.ch/api/v4/projects/%s"

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

    default_branch = response.json()[
        "default_branch" if not gitlab else "default_branch"
    ]

    return default_branch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add latest commits to a spack environment"
    )
    parser.add_argument(
        "--path",
        help="path to a yaml file with spack packages",
    )
    parser.add_argument(
        "--extra-path",
        help="path to a yaml file with spack packages",
    )
    parser.add_argument(
        "date",
        help="date until which to search for commits, for example: 2021-01-01",
        default=None,
    )
    args = parser.parse_args()
    date = args.date

    try:
        with open(args.path, "r") as recipe:
            text = yaml.safe_load(recipe)
    except FileNotFoundError:
        print("Please run this script from the key4hep-spack repository.")
        raise

    try:
        with open(args.extra_path, "r") as recipe:
            text_extra = yaml.safe_load(recipe)
    except FileNotFoundError:
        print("Please run this script from the key4hep-spack repository.")
        raise

    for package, location in [
        ("aidatt", "aidasoft/aidatt"),
        ("ced", "ilcsoft/ced"),
        ("cedviewer", "ilcsoft/cedviewer"),
        # ("cepcsw", "cepc/cepcsw"),
        ("clicperformance", "ilcsoft/clicperformance"),
        ("conformaltracking", "ilcsoft/conformaltracking"),
        ("dd4hep", "aidasoft/dd4hep"),
        ("ddkaltest", "ilcsoft/ddkaltest"),
        ("ddmarlinpandora", "ilcsoft/ddmarlinpandora"),
        ("delphes", "delphes/delphes"),
        ("dual-readout", "hep-fcc/dual-readout"),
        ("edm4hep", "key4hep/edm4hep"),
        ("fcalclusterer", "fcalsw/fcalclusterer"),
        ("fccanalyses", "hep-fcc/fccanalyses"),
        ("fccdetectors", "hep-fcc/fccdetectors"),
        ("fccsw", "hep-fcc/fccsw"),
        ("forwardtracking", "ilcsoft/forwardtracking"),
        ("gear", "ilcsoft/gear"),
        ("ilcutil", "ilcsoft/ilcutil"),
        ("ildperformance", "ilcsoft/ildperformance"),
        ("k4clue", "key4hep/k4clue"),
        ("k4edm4hep2lcioconv", "key4hep/k4edm4hep2lcioconv"),
        ("k4fwcore", "key4hep/k4fwcore"),
        ("k4gen", "hep-fcc/k4Gen"),
        ("k4geo", "key4hep/k4geo"),
        ("k4marlinwrapper", "key4hep/k4marlinwrapper"),
        ("k4projecttemplate", "key4hep/k4-project-template"),
        ("k4reccalorimeter", "hep-fcc/k4reccalorimeter"),
        ("k4rectracker", "key4hep/k4rectracker"),
        ("k4simdelphes", "key4hep/k4SimDelphes"),
        ("k4simgeant4", "hep-fcc/k4simgeant4"),
        ("kaltest", "ilcsoft/kaltest"),
        ("kitrack", "ilcsoft/kitrack"),
        ("kitrackmarlin", "ilcsoft/kitrackmarlin"),
        ("lccd", "ilcsoft/lccd"),
        ("lcfiplus", "lcfiplus/lcfiplus"),
        ("lcio", "ilcsoft/lcio"),
        ("lctuple", "ilcsoft/lctuple"),
        ("marlindd4hep", "ilcsoft/marlindd4hep"),
        ("marlinfastjet", "ilcsoft/marlinfastjet"),
        ("marlin", "ilcsoft/marlin"),
        ("marlinkinfit", "ilcsoft/marlinkinfit"),
        ("marlinkinfitprocessors", "ilcsoft/marlinkinfitprocessors"),
        ("marlinreco", "ilcsoft/marlinreco"),
        ("marlintrk", "ilcsoft/marlintrk"),
        ("marlintrkprocessors", "ilcsoft/marlintrkprocessors"),
        ("marlinutil", "ilcsoft/marlinutil"),
        ("opendatadetector", "acts/OpenDataDetector"),
        ("overlay", "ilcsoft/overlay"),
        ("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis"),
        ("physsim", "ilcsoft/physsim"),
        ("podio", "aidasoft/podio"),
        ("raida", "ilcsoft/raida"),
        ("sio", "ilcsoft/sio"),
    ]:
        gitlab = False
        if package in ["opendatadetector"]:
            gitlab = True
        commit = get_default_branch(package, location, gitlab=gitlab, date=date)
        line = f"@{commit} "
        # if package not in ["cepcsw"]:
        #     line += "=develop"
        original = " "
        if package in text["packages"] and "require" in text["packages"][package]:
            original = text["packages"][package]["require"]
            text["packages"][package]["require"] = line + original
        elif (
            package in text_extra["packages"]
            and "require" in text_extra["packages"][package]
        ):
            original = text_extra["packages"][package]["require"]
            text_extra["packages"][package]["require"] = line + original
        else:
            text_extra["packages"][package]["require"] = line

    with open(args.path, "w") as recipe:
        yaml.dump(text, recipe)
    with open(args.extra_path, "w") as recipe:
        yaml.dump(text_extra, recipe)
