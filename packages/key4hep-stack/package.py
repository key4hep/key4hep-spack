from spack import *
from datetime import datetime
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_dependency 


class Key4hepStack(BundlePackage):
    """Bundle package to install the Key4hep software stack."""
    
    homepage = 'https://cern.ch/key4hep'

    ##################### versions ########################
    #######################################################
    # tries to build the HEAD of each package.
    # used for master builds
    version('master')
    # the preferred usage is to use the date as versio, like: 
    # builds the latest stable version of each package
    # the preferred usage is to use the date as version, see below
    #version('master-2020-10-06')
    version(datetime.today().strftime('%Y-%m-%d'))
    #version('2020-10-06') # example, no need to add them here

    ##################### variants ########################
    #######################################################
    variant('devtools', default=True,
            description="add tools necessary for software masterment to the stack")
    variant('generators', default=False,
            description="add some standalone generators to the stack")
    variant('bootstrap', default=True,
            description="install some spack setup tools")
    

    ##################### common key4hep packages #########
    #######################################################
    depends_on('edm4hep')
    k4_add_latest_commit_as_dependency("edm4hep", "key4hep/edm4hep", when="@master")

    depends_on('podio')
    #k4_add_latest_commit_as_dependency("podio", "aidasoft/podio", when="@master")
    depends_on("podio@master", when="@master")

    depends_on("k4fwcore")
    k4_add_latest_commit_as_dependency("k4fwcore", "key4hep/k4fwcore", when="@master")
    
    depends_on("guinea-pig")
    # todo: figure out the api for the cern gitlab instance
    #depends_on('guinea-pig@master', when="@master")

    depends_on('whizard +lcio +openloops hepmc=2')
    # todo: figure out the api for the whizard gitlab instance
    #depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on("delphes")
    #k4_add_latest_commit_as_dependency("delphes", "delphes/delphes", when="@master")
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
    k4_add_latest_commit_as_dependency("aidatt", "aidasoft/aidatt", when="@master")

    depends_on('cedviewer')
    k4_add_latest_commit_as_dependency("cedviewer", "ilcsoft/cedviewer", when="@master")

    depends_on('conformaltracking')
    k4_add_latest_commit_as_dependency("conformaltracking", "ilcsoft/conformaltracking", when="@master")

    depends_on('clicperformance')
    k4_add_latest_commit_as_dependency("clicperformance", "ilcsoft/clicperformance", when="@master")

    depends_on('clupatra')
    k4_add_latest_commit_as_dependency("clupatra", "ilcsoft/clupatra", when="@master")

    depends_on('ced')
    k4_add_latest_commit_as_dependency("ced", "ilcsoft/ced", when="@master")

    depends_on('ddkaltest')
    k4_add_latest_commit_as_dependency("ddkaltest", "ilcsoft/ddkaltest", when="@master")

    depends_on('ddmarlinpandora')
    k4_add_latest_commit_as_dependency("ddmarlinpandora", "ilcsoft/ddmarlinpandora", when="@master")

    depends_on('fcalclusterer')
    k4_add_latest_commit_as_dependency("fcalclusterer", "fcalsw/fcalclusterer", when="@master")

    depends_on('forwardtracking')
    k4_add_latest_commit_as_dependency("forwardtracking", "ilcsoft/forwardtracking", when="@master")

    depends_on('garlic')
    k4_add_latest_commit_as_dependency("garlic", "ilcsoft/garlic", when="@master")

    depends_on('gaudimarlinwrapper')
    k4_add_latest_commit_as_dependency("gaudimarlinwrapper", "key4hep/gmp", when="@master")

    depends_on('generalbrokenlines')
    k4_add_latest_commit_as_dependency("generalbrokenlines", "GeneralBrokenLines/GeneralBrokenLines", when="@master")

    depends_on('gear')
    k4_add_latest_commit_as_dependency("gear", "ilcsoft/gear", when="@master")

    depends_on('ilcutil')
    k4_add_latest_commit_as_dependency("ilcutil", "ilcsoft/ilcutil", when="@master")

    depends_on('ildperformance')
    k4_add_latest_commit_as_dependency("ildperformance", "ilcsoft/ildperformance", when="@master")

    depends_on('kaldet')
    k4_add_latest_commit_as_dependency("kaldet", "ilcsoft/kaldet", when="@master")

    depends_on('kitrackmarlin')
    k4_add_latest_commit_as_dependency("kitrackmarlin", "ilcsoft/kitrackmarlin", when="@master")

    depends_on('kaltest')
    k4_add_latest_commit_as_dependency("kaltest", "ilcsoft/kaltest", when="@master")

    depends_on('kitrack')
    k4_add_latest_commit_as_dependency("kitrack", "ilcsoft/kitrack", when="@master")

    depends_on('lcfiplus')
    k4_add_latest_commit_as_dependency("lcfiplus", "lcfiplus/lcfiplus", when="@master")

    depends_on('lctuple')
    k4_add_latest_commit_as_dependency("lctuple", "ilcsoft/lctuple", when="@master")

    depends_on('lcfivertex')
    k4_add_latest_commit_as_dependency("lcfivertex", "ilcsoft/lcfivertex", when="@master")

    depends_on('lich')
    k4_add_latest_commit_as_dependency("lich", "danerdaner/lich", when="@master")

    depends_on('lccd')
    k4_add_latest_commit_as_dependency("lccd", "ilcsoft/lccd", when="@master")

    depends_on('lcio')
    #k4_add_latest_commit_as_dependency("lcio", "ilcsoft/lcio", when="@master")
    #depends_on("lcio@master", when="@master")

    depends_on('lcgeo')
    k4_add_latest_commit_as_dependency("lcgeo", "ilcsoft/lcgeo", when="@master")

    depends_on('marlin')
    k4_add_latest_commit_as_dependency("marlin", "ilcsoft/marlin", when="@master")

    depends_on('marlinutil')
    k4_add_latest_commit_as_dependency("marlinutil", "ilcsoft/marlinutil", when="@master")

    depends_on('marlinpandora')
    k4_add_latest_commit_as_dependency("marlinpandora", "pandorapfa/marlinpandora", when="@master")

    depends_on("marlindd4hep")
    k4_add_latest_commit_as_dependency("marlindd4hep", "ilcsoft/marlindd4hep", when="@master")

    depends_on('marlinreco')
    k4_add_latest_commit_as_dependency("marlinreco", "ilcsoft/marlinreco", when="@master")

    depends_on('marlinfastjet')
    k4_add_latest_commit_as_dependency("marlinfastjet", "ilcsoft/marlinfastjet", when="@master")

    depends_on('marlinkinfit')
    k4_add_latest_commit_as_dependency("marlinkinfit", "ilcsoft/marlinkinfit", when="@master")

    depends_on('marlintrkprocessors')
    k4_add_latest_commit_as_dependency("marlintrkprocessors", "ilcsoft/marlintrkprocessors", when="@master")

    depends_on('marlintrk')
    k4_add_latest_commit_as_dependency("marlintrk", "ilcsoft/marlintrk", when="@master")

    depends_on('overlay')
    k4_add_latest_commit_as_dependency("overlay", "ilcsoft/overlay", when="@master")

    depends_on('pandoraanalysis')
    k4_add_latest_commit_as_dependency("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", when="@master")

    depends_on('pandorapfa')
    k4_add_latest_commit_as_dependency("pandorapfa", "pandorapfa/pandorapfa", when="@master")


    depends_on('physsim')
    k4_add_latest_commit_as_dependency("physsim", "ilcsoft/physsim", when="@master")

    depends_on("raida")
    k4_add_latest_commit_as_dependency("raida", "ilcsoft/raida", when="@master")

    depends_on('sio')
    k4_add_latest_commit_as_dependency("sio", "ilcsoft/sio", when="@master")


    ############################### fccsw #################
    #######################################################
    depends_on("fccsw")
    k4_add_latest_commit_as_dependency("fccsw", "hep-fcc/fccsw", when="@master")

    depends_on("fcc-edm")
    k4_add_latest_commit_as_dependency("fcc-edm", "hep-fcc/fcc-edm", when="@master")

    depends_on("dual-readout")
    k4_add_latest_commit_as_dependency("dual-readout", "hep-fcc/dual-readout", when="@master")

    ############################## cepcsw #################
    #######################################################
    depends_on("cepcsw")
    k4_add_latest_commit_as_dependency("cepcsw", "cepc/cepcsw", when="@master")


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

    
