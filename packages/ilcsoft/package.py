from datetime import datetime

from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import install_setup_script


class Ilcsoft(BundlePackage, Key4hepPackage):
    """Bundle package to install Ilcsoft"""

    homepage = "https://cern.ch/key4hep"

    ##################### versions ########################
    #######################################################
    ###  nightly builds
    version("master")
    # this version can be extended with additional version
    # fields to differentiate it, like 'master-2020-10-10'
    #
    ### stable builds
    # builds the latest release of each package
    # the preferred usage is to use the date as version, like:
    version(datetime.today().strftime("%Y-%m-%d"))
    # version('2020-10-06') # example, no need to add here.
    # more complex version configurations should be added in an
    # environment

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ["install"]

    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
    )

    ############################### key4hep ###############
    #######################################################

    depends_on("guinea-pig")
    # todo: figure out the api for the cern gitlab instance
    # depends_on('guinea-pig@master', when="@master")

    depends_on("whizard +lcio +openloops hepmc=2")
    # todo: figure out the api for the whizard gitlab instance
    # depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on("k4lcioreader")
    depends_on("k4simdelphes")
    depends_on("delphes")

    ############################### ilcsoft ###############
    #######################################################
    depends_on("aidatt")
    depends_on("cedviewer")
    depends_on("conformaltracking")
    depends_on("clicperformance")
    depends_on("clupatra")
    depends_on("ced")
    depends_on("ddkaltest")
    depends_on("ddmarlinpandora")
    depends_on("fcalclusterer")
    depends_on("forwardtracking")
    depends_on("garlic")
    depends_on("k4marlinwrapper")
    depends_on("generalbrokenlines")
    depends_on("gear")
    depends_on("ilcutil")
    depends_on("ildperformance")
    depends_on("kaldet")
    depends_on("kitrackmarlin")
    depends_on("kaltest")
    depends_on("kitrack")
    depends_on("lcfiplus")
    depends_on("lctuple")
    depends_on("lcfivertex")
    depends_on("lccd")
    depends_on("lcio")
    depends_on("k4geo")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("marlindd4hep")
    depends_on("marlinreco")
    depends_on("marlinfastjet")
    depends_on("marlinkinfit")
    depends_on("marlinkinfitprocessors")
    depends_on("marlintrkprocessors")
    depends_on("marlintrk")
    depends_on("overlay")
    depends_on("pandoraanalysis")
    depends_on("pandorapfa")
    depends_on("physsim")
    depends_on("raida")
    depends_on("sio")

    ##################### developer tools #################
    #######################################################
    depends_on("cmake")
    depends_on("ninja")

    ##################### conflicts #######################
    #######################################################
    conflicts(
        "%gcc@8.3.1",
        msg="There are known issues with compilers from redhat's devtoolsets"
        "which are therefore not supported."
        "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286",
    )

    def setup_run_environment(self, env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        env.set("LC_ALL", "C")

    # def install(self, spec, prefix):
    #     return install_setup_script(self, spec, prefix, "ILCSOFT_LATEST_SETUP_PATH")
