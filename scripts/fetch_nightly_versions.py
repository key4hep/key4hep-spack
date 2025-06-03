import os
import requests
import argparse
import yaml
from datetime import datetime


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
    print(f"Fetching the latest commit for {name}")
    if gitlab:
        giturl = gitlab
    else:
        giturl = "https://api.github.com/repos/%s/commits"

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
    if not response.ok:
        print("Request failed")

    commit = response.json()[0]["sha" if not gitlab else "id"]
    int(commit, 16)

    return commit


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add latest commits to a spack environment"
    )

    # There are commented blocks to write to the packages.yaml directly and
    # having a single spec instead of having multiple However, spack keeps
    # having issues when concretizing on top of an existing installation (that may not be complete)
    # so I'm reverting back to the previous approach of having multiple specs

    parser.add_argument(
        "--path",
        help="path to a yaml file with spack packages",
    )
    parser.add_argument(
        "--extra-path",
        help="path to a yaml file with spack packages",
    )
    parser.add_argument(
        "--only-merge",
        help="only merge the packages.yaml files",
        action="store_true",
    )
    # parser.add_argument(
    #     "--spack",
    #     help="path to the spack.yaml in the nightly environment",
    # )
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

    # try:
    #     with open(args.spack, "r") as config:
    #         text = yaml.safe_load(config)
    # except FileNotFoundError:
    #     print("Please run this script from the key4hep-spack repository.")
    #     raise

    for package, location in [
        ("acts", "acts-project/acts"),
        ("aidatt", "aidasoft/aidatt"),
        ("ced", "ilcsoft/ced"),
        ("cedviewer", "ilcsoft/cedviewer"),
        # ("cepcsw", "cepc/cepcsw"),
        ("cldconfig", "key4hep/CLDConfig"),
        ("clicperformance", "ilcsoft/clicperformance"),
        ("conformaltracking", "ilcsoft/conformaltracking"),
        ("dd4hep", "aidasoft/dd4hep"),
        ("ddfastshowerml", "ilcsoft/ddfastshowerml"),
        ("ddkaltest", "ilcsoft/ddkaltest"),
        ("ddmarlinpandora", "ilcsoft/ddmarlinpandora"),
        ("delphes", "delphes/delphes"),
        ("dual-readout", "hep-fcc/dual-readout"),
        ("edm4hep", "key4hep/edm4hep"),
        ("fcalclusterer", "fcalsw/fcalclusterer"),
        ("fccanalyses", "hep-fcc/fccanalyses"),
        ("fcc-config", "hep-fcc/fcc-config"),
        ("fccdetectors", "hep-fcc/fccdetectors"),
        ("fccsw", "hep-fcc/fccsw"),
        ("forwardtracking", "ilcsoft/forwardtracking"),
        ("gear", "ilcsoft/gear"),
        ("ilcutil", "ilcsoft/ilcutil"),
        ("ildperformance", "ilcsoft/ildperformance"),
        ("k4mljettagger", "key4hep/k4mljettagger"),
        ("k4clue", "key4hep/k4clue"),
        ("k4edm4hep2lcioconv", "key4hep/k4edm4hep2lcioconv"),
        ("k4fwcore", "key4hep/k4fwcore"),
        ("k4gaudipandora", "key4hep/k4gaudipandora"),
        ("k4gen", "hep-fcc/k4Gen"),
        ("k4generatorsconfig", "key4hep/k4GeneratorsConfig"),
        ("k4geo", "key4hep/k4geo"),
        ("k4reco", "key4hep/k4reco"),
        ("k4marlinwrapper", "key4hep/k4marlinwrapper"),
        ("k4projecttemplate", "key4hep/k4-project-template"),
        ("k4reccalorimeter", "hep-fcc/k4reccalorimeter"),
        ("k4rectracker", "key4hep/k4rectracker"),
        ("k4simdelphes", "key4hep/k4SimDelphes"),
        ("k4simgeant4", "key4hep/k4simgeant4"),
        ("kaltest", "ilcsoft/kaltest"),
        ("kitrack", "ilcsoft/kitrack"),
        ("kitrackmarlin", "ilcsoft/kitrackmarlin"),
        ("lccd", "ilcsoft/lccd"),
        ("lcfiplus", "lcfiplus/lcfiplus"),
        ("lcio", "ilcsoft/lcio"),
        ("lctuple", "ilcsoft/lctuple"),
        ("marlin", "ilcsoft/marlin"),
        ("marlindd4hep", "ilcsoft/marlindd4hep"),
        ("marlinfastjet", "ilcsoft/marlinfastjet"),
        ("marlinkinfit", "ilcsoft/marlinkinfit"),
        ("marlinkinfitprocessors", "ilcsoft/marlinkinfitprocessors"),
        ("marlinmlflavortagging", "ilcsoft/marlinmlflavortagging"),
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
        ("simsipm", "edopro98/simsipm"),
        ("sio", "ilcsoft/sio"),
    ]:
        if args.only_merge:
            break
        gitlab = False
        if package == "opendatadetector":
            gitlab = "https://gitlab.cern.ch/api/v4/projects/%s/repository/commits"
        elif package == "ddfastshowerml" or package == "marlinmlflavortagging":
            gitlab = "https://gitlab.desy.de/api/v4/projects/%s/repository/commits"
        commit = get_latest_commit(package, location, date=date, gitlab=gitlab)
        line = f"@{commit}"
        if package not in ["cepcsw"]:
            line += "=develop"

        if package not in text["packages"] or not text["packages"][package]:
            print(f"Adding {package}@{commit} to the key4hep-stack package.py")
        else:
            print(f"Updating {package}@{commit} in the key4hep-stack package.py")

        if package not in text["packages"]:
            text["packages"][package] = {}
        text["packages"][package]["require"] = (
            line + " " + text["packages"][package].get("require", "")
        )

    all_packages = set(text["packages"].keys()).union(
        set(text_extra["packages"].keys())
    )
    for package in all_packages:
        # Make sure the require options are merged in a single file, because
        # otherwise they would be overwritten
        final_text = ""
        if package in text["packages"] and "require" in text["packages"][package]:
            final_text += text["packages"][package]["require"]
        if (
            package in text_extra["packages"]
            and "require" in text_extra["packages"][package]
        ):
            final_text += " " + text_extra["packages"][package].pop("require")
        if package not in text["packages"]:
            text["packages"][package] = {}
        text["packages"][package]["require"] = final_text
    if "key4hep-stack" not in text["packages"]:
        text["packages"]["key4hep-stack"] = {}
    text["packages"]["key4hep-stack"][
        "require"
    ] = f"@{datetime.now().strftime('%Y-%m-%d')}: " + text["packages"][
        "key4hep-stack"
    ].get(
        "require", ""
    )

    with open(args.path, "w") as recipe:
        yaml.dump(text, recipe)
    with open(args.extra_path, "w") as recipe:
        yaml.dump(text_extra, recipe)
    # with open(args.spack, "w") as config:
    #     yaml.dump(text, config)
