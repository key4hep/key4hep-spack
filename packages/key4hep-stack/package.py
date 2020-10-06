from spack import *
from spack.package import PackageBase
from datetime import datetime


class Key4hepStack(BundlePackage):
    """Bundle package to install the Key4hep software stack."""
    
    homepage = 'https://cern.ch/key4hep'

    ##################### versions ########################
    #######################################################
    # tries to build the HEAD of each package.
    # used for master builds
    version('master')
    # builds the latest stable version of each package
    # the preferred usage is to use the date as version, see below
    version(datetime.today().strftime('%Y-%m-%d'))
    #version('2020-10-06') # example, no need to add them here

    ##################### variants ########################
    #######################################################
    variant('devtools', default=True,
            description="add tools necessary for software masterment to the stack")
    variant('generators', default=True,
            description="add some standalone generators to the stack")
    variant('fccsw', default=True,
            description="build fcc packages")
    variant('ilcsoft', default=True,
            description="build ilcsoft packages")
    variant('bootstrap', default=True,
            description="install some spack setup tools")
    

    ##################### common key4hep packages #########
    #######################################################
    depends_on('edm4hep')
    depends_on('edm4hep@master', when="@master")

    depends_on('podio')
    depends_on('podio@master', when="@master")

    depends_on("K4FWCore")
    depends_on('K4FWCore@master', when="@master")
    
    depends_on("guinea-pig")
    depends_on('guinea-pig@master', when="@master")

    depends_on('whizard +lcio +openloops hepmc=2')
    depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on("delphes")
    depends_on("delphes@master", when="@master")
    ##################### general purpose generators ######
    #######################################################
    depends_on("madgraph5amc", when="+generators")
    depends_on("herwigpp", when="+generators")
    # todo: investigate build failure with newer versions
    depends_on("lhapdf@6.2.3", when="+generators")



    ############################### ilcsoft ###############
    #######################################################
    depends_on('aidatt')
    depends_on('aidatt@master', when="@master")

    depends_on('cedviewer')
    depends_on('cedviewer@master', when="@master")

    depends_on('conformaltracking')
    depends_on('conformaltracking@master', when="@master")

    depends_on('clicperformance')
    depends_on('clicperformance@master', when="@master")

    depends_on('clupatra')
    depends_on('clupatra@master', when='@master')

    depends_on('ced')
    depends_on('ced@master', when='@master')

    depends_on('ddkaltest')
    depends_on('ddkaltest@master', when='@master')


    depends_on('ddmarlinpandora')
    depends_on('ddmarlinpandora@master', when='@master')

    depends_on('fcalclusterer')
    depends_on('fcalclusterer@master', when="@master")

    depends_on('forwardtracking')
    depends_on('forwardtracking@master', when="@master")

    depends_on('garlic')
    depends_on('garlic@master', when="@master")

    depends_on('gaudimarlinwrapper')
    depends_on('gaudimarlinwrapper@master', when="@master")

    depends_on('generalbrokenlines')
    depends_on('generalbrokenlines@master', when='@master')

    depends_on('gear')
    depends_on('gear@master', when='@master')

    depends_on('ilcutil')
    depends_on('ilcutil@master', when='@master')

    depends_on('ildperformance')
    depends_on('ildperformance@master', when='@master')

    depends_on('kaldet')
    depends_on('kaldet@master', when="@master")

    depends_on('kitrackmarlin')
    depends_on('kitrackmarlin@master', when="@master")

    depends_on('kaltest')
    depends_on('kaltest@master', when='@master')

    depends_on('kitrack')
    depends_on('kitrack@master', when='@master')

    depends_on('lcfiplus')
    depends_on('lcfiplus@master', when='@master')

    depends_on('lctuple')
    depends_on('lctuple@master', when='@master')

    depends_on('lcfivertex')
    depends_on('lcfivertex@master', when='@master')

    depends_on('lich')
    depends_on('lich@master', when='@master')

    depends_on('lccd')
    depends_on('lccd@master', when='@master')

    depends_on('lcio')
    depends_on('lcio@master', when="@master")

    depends_on('lcgeo')
    depends_on('lcgeo@master', when="@master")

    depends_on('marlin')
    depends_on('marlin@master', when="@master")

    depends_on('marlinutil')
    depends_on('marlinutil@master', when="@master")

    depends_on('marlinpandora')
    depends_on('marlinpandora@master', when="@master")

    depends_on("marlindd4hep")
    depends_on('marlindd4hep@master', when='@master')

    depends_on('marlinreco')
    depends_on('marlinreco@master', when='@master')

    depends_on('marlinfastjet')
    depends_on('marlinfastjet@master', when='@master')

    depends_on('marlinkinfit')
    depends_on('marlinkinfit@master', when='@master')

    depends_on('marlintrkprocessors')
    depends_on('marlintrkprocessors@master', when='@master')

    depends_on('marlintrk')
    depends_on('marlintrk@master', when='@master')

    depends_on('overlay')
    depends_on('overlay@master', when='@master')

    depends_on('pandoraanalysis')
    depends_on('pandoraanalysis@master', when='@master')

    depends_on('pandorapfa')
    depends_on('pandorapfa@master', when="@master")

    depends_on('physsim')
    depends_on('physsim@master', when="@master")

    depends_on("raida")
    depends_on('raida@master', when='@master')

    depends_on('sio')
    depends_on('sio@master', when='@master')


    ############################### fccsw #################
    #######################################################
    depends_on("fccsw")
    depends_on("fccsw@master", when='@master')

    depends_on("fcc-edm")
    depends_on("fcc-edm@master", when="@master")

    depends_on("dual-readout")
    depends_on("dual-readout@master", when="@master")

    ##################### developer tools #################
    #######################################################
    depends_on("cmake", when="+devtools")
    depends_on("gdb", "when=+devtools")
    depends_on("emacs+X toolkit=athena", when="+devtools")
    depends_on("ninja", when="+devtools")
    depends_on("py-ipython", when="+devtools")

    ##################### environment boostrap ############
    #######################################################
    depends_on("environment-modules", when="+bootstrap")


    ##################### conflicts #######################
    #######################################################
    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    

