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
    depends_on('podio')
    depends_on('dd4hep')
    depends_on('k4fwcore')
    depends_on('k4projecttemplate')

    depends_on('k4simdelphes')
    depends_on('lcgeo')
    depends_on('k4gen')
    depends_on('k4lcioreader')
    depends_on('k4simgeant4')
    depends_on('k4clue')
    depends_on('k4actstracking')
    depends_on('k4edm4hep2lcioconv')

    depends_on('bdsim')
    depends_on('guinea-pig')
    depends_on('whizard +lcio +openloops hepmc=2')
    depends_on('kkmcee')
    depends_on('bhlumi')
    depends_on('babayaga')
    depends_on('delphes')

    depends_on('xrootd +krb5')
    depends_on('python~debug')

    ##################### general purpose generators ######
    #######################################################
    depends_on('madgraph5amc', when='+generators')
    depends_on('herwig3', when='+generators')
    depends_on('lhapdf', when='+generators')
    depends_on('sherpa', when='+generators')
    depends_on('photos+hepmc3', when='+generators')

    ############################### ilcsoft ###############
    #######################################################
    depends_on('ilcsoft')

    ############################### fccsw #################
    #######################################################
    depends_on('fccsw')
    depends_on('dual-readout')
    depends_on('fccanalyses')
    depends_on('fccdetectors')
    depends_on('k4reccalorimeter')

    ############################## cepcsw #################
    #######################################################
    depends_on('cepcsw')
    
    ##################### developer tools #################
    #######################################################
    depends_on('catch2@3.0.1:', when='+devtools')
    depends_on('cmake', when='+devtools')
    depends_on('man-db', when='+devtools')
    depends_on('gdb', when='+devtools')
    depends_on('ninja', when='+devtools')
    depends_on('py-ipython', when='+devtools')
    depends_on('doxygen', when='+devtools')
    #depends_on('prmon', when='+devtools')
    depends_on('py-pip', when='+devtools')
    depends_on('py-particle', when='+devtools')
    depends_on('py-awkward', when='+devtools')
    depends_on('py-matplotlib', when='+devtools')
    depends_on('py-uproot', when='+devtools')
    depends_on('py-pandas', when='+devtools')
    depends_on('py-scipy', when='+devtools')

    depends_on('py-scikit-learn', when='+devtools')
    depends_on('xgboost', when='+devtools')
    depends_on('onnx', when='+devtools')
    depends_on('py-onnx', when='+devtools')
    depends_on('py-onnx-runtime', when='+devtools')
    #depends_on('py-pyg4ometry', when='+devtools')
    #depends_on('py-tensorflow') # todo: check if we should integrate.
    #depends_on('py-zfit') # todo: add in spack
    #depends_on('py-root-pandas') # todo: add in spack

    # tools for doctests
    depends_on('py-jupytext', when='+devtools')
    depends_on('py-nbconvert', when='+devtools')
    depends_on('py-ipykernel', when='+devtools')


    ##################### environment boostrap ############
    #######################################################
    depends_on('environment-modules', when='+bootstrap')


    ##################### conflicts #######################
    #######################################################
    conflicts('%gcc@8.3.1',
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    ##################### other spack funcs################
    #######################################################

    def setup_run_environment(self, spack_env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        spack_env.set('LC_ALL', 'C')
        spack_env.set('KEY4HEP_STACK', os.path.join(self.spec.prefix, 'setup.sh'))

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, 'K4_LATEST_SETUP_PATH')
