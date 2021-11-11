from datetime import datetime
import os

# import common methods for use in recipe from common.py
# (so other recipe can import from spack.pkg.k4.key4hep_stack)
# (which is the most convenient way to make that code available
#  without creation of a new module
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from common import *

class Key4hepStack(BundlePackage, Key4hepPackage):
    """Bundle package to install the Key4hep software stack."""
    
    homepage = 'https://cern.ch/key4hep'

    ##################### versions ########################
    #######################################################
    ###  nightly builds
    # builds the HEAD of each package for which 
    # k4_add_latest_commit_as_dependency is called below
    version('master')
    # this version can be extended with additional version
    # fields to differentiate it, like 'master-2020-10-10'
    #
    ### stable builds
    # builds the latest release of each package
    # the preferred usage is to use the date as version, like:
    version(datetime.today().strftime('%Y-%m-%d'))
    #version('2020-10-06') # example, no need to add here.
    # more complex version configurations should be added in an
    # environment

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ['install']

    ##################### variants ########################
    #######################################################
    variant('devtools', default=True,
            description="add tools necessary for software development to the stack")
    variant('generators', default=True,
            description="add some standalone generators to the stack")
    variant('bootstrap', default=False,
            description="install some spack setup tools")
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    

    ##################### common key4hep packages #########
    #######################################################
    depends_on('edm4hep')
    k4_add_latest_commit_as_dependency("edm4hep", "key4hep/edm4hep", when="@master")

    depends_on('podio')
    # TODO: temporarily disable due to known issue with https://github.com/AIDASoft/podio/pull/193
    #k4_add_latest_commit_as_dependency("podio", "aidasoft/podio", when="@master")

    depends_on('dd4hep')
    k4_add_latest_commit_as_dependency("dd4hep", "aidasoft/dd4hep", when="@master")

    depends_on("k4fwcore")
    k4_add_latest_commit_as_dependency("k4fwcore", "key4hep/k4fwcore", when="@master")

    depends_on("k4projecttemplate")
    k4_add_latest_commit_as_dependency("k4projecttemplate", "key4hep/k4-project-template", when="@master")


    depends_on("k4simdelphes")
    k4_add_latest_commit_as_dependency("k4simdelphes", "key4hep/k4SimDelphes", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    depends_on("k4gen")
    k4_add_latest_commit_as_dependency("k4gen", "hep-fcc/k4Gen", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    depends_on("k4simgeant4")
    k4_add_latest_commit_as_dependency("k4simgeant4", "hep-fcc/k4simgeant4", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    depends_on("k4clue")
    k4_add_latest_commit_as_dependency("k4clue", "key4hep/k4clue", when="@master")

    depends_on('k4actstracking')

    depends_on("guinea-pig")
    # todo: figure out the api for the cern gitlab instance
    #depends_on('guinea-pig@master', when="@master")

    depends_on('whizard +lcio +openloops hepmc=2')
    # todo: figure out the api for the whizard gitlab instance
    #depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on('kkmcee')

    depends_on('bhlumi')

    depends_on('babayaga')

    depends_on("delphes")
    # wait for issues in delphes master to be fixed
    k4_add_latest_commit_as_dependency("delphes", "delphes/delphes", when="@master")

    ##################### general purpose generators ######
    #######################################################
    depends_on("madgraph5amc", when="+generators")
    depends_on("herwig3", when="+generators")
    # todo: investigate build failure with newer versions
    depends_on("lhapdf@6.2.3", when="+generators")


    ############################### ilcsoft ###############
    #######################################################

    depends_on("ilcsoft")
    depends_on("ilcsoft@master", when="@master")


    ############################### fccsw #################
    #######################################################
    depends_on("fccsw")
    k4_add_latest_commit_as_dependency("fccsw", "hep-fcc/fccsw", when="@master")


    #depends_on("dual-readout")
    #k4_add_latest_commit_as_dependency("dual-readout", "hep-fcc/dual-readout", when="@master")


    depends_on("fccanalyses")
    k4_add_latest_commit_as_dependency("fccanalyses", "hep-fcc/fccanalyses", when="@master")

    depends_on("fccdetectors")
    k4_add_latest_commit_as_dependency("fccdetectors", "hep-fcc/fccdetectors", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    depends_on("k4reccalorimeter")
    k4_add_latest_commit_as_dependency("k4reccalorimeter", "hep-fcc/k4reccalorimeter", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    ############################## cepcsw #################
    #######################################################
    depends_on("cepcsw")
    k4_add_latest_commit_as_dependency("cepcsw", "cepc/cepcsw", when="@master")
    
    depends_on("k4lcioreader")
    k4_add_latest_commit_as_dependency("k4lcioreader", "key4hep/k4LCIOReader", when="@master")


    ##################### developer tools #################
    #######################################################
    depends_on("catch2@3.0.1:", when="+devtools")
    depends_on("cmake", when="+devtools")
    depends_on('man-db', when="+devtools")
    depends_on("gdb", when="+devtools")
    depends_on("emacs+X toolkit=athena", when="+devtools")
    depends_on("ninja", when="+devtools")
    depends_on("py-ipython", when="+devtools")
    depends_on("doxygen", when="+devtools")
    depends_on("py-pip", when="+devtools")
    depends_on('py-particle', when="+devtools")
    depends_on('py-awkward', when="+devtools")
    depends_on('py-matplotlib', when="+devtools")
    depends_on('py-uproot', when="+devtools")
    depends_on('py-pandas', when="+devtools")
    depends_on('py-scikit-learn', when="+devtools")
    depends_on('py-scipy', when="+devtools")
    depends_on('xgboost', when="+devtools")
    #depends_on('py-pyg4ometry', when="+devtools")
    #depends_on('py-tensorflow') # todo: check if we should integrate.
    #depends_on('py-zfit') # todo: add in spack
    #depends_on('py-root-pandas') # todo: add in spack


    ##################### environment boostrap ############
    #######################################################
    depends_on("environment-modules", when="+bootstrap")


    ##################### conflicts #######################
    #######################################################
    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    def setup_run_environment(self, spack_env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        spack_env.set("LC_ALL", "C")

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, 'K4_LATEST_SETUP_PATH')
