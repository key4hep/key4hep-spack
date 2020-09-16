from spack import *
from spack.package import PackageBase

class Key4hepStack(BundlePackage):
    """Bundle package to install the Key4hep software development environment."""
    
    
    homepage = 'https://cern.ch/key4hep'
    
    version('0.1')
    version('nightly')

    
    depends_on('podio@master', when="@nightly")
    depends_on('edm4hep@master', when="@nightly")
    depends_on('K4FWCore@master', when="@nightly")
    depends_on('guinea-pig@master', when="@nightly")
    depends_on('lcgeo', when="@nightly")
    depends_on("dd4hep@master +lcio", when="@nightly")
    
    depends_on("edm4hep@0.2.0", when="@0.1")
    depends_on("K4FWCore@0.1.0", when="@0.1")
    depends_on('guinea-pig@1.2.2rc', when="@0.1")
    depends_on('whizard +lcio +openloops', when="@0.1")

    depends_on('lcio', when="@0.1")
    depends_on('dd4hep +lcio', when="@0.1")
    depends_on('lcgeo', when="@0.1")

    depends_on('marlin', when="@0.1")
    depends_on('gaudimarlinwrapper', when="@0.1")
    depends_on('marlinutil', when="@0.1")
    depends_on('aidatt', when="@0.1")
    depends_on('physsim', when="@0.1")
    depends_on('cedviewer', when="@0.1")
    depends_on('conformaltracking', when="@0.1")
    depends_on('forwardtracking', when="@0.1")
    depends_on('kaldet', when="@0.1")
    depends_on('kitrackmarlin', when="@0.1")
    depends_on('marlinpandora', when="@0.1")
    depends_on('pandorapfa', when="@0.1")
    depends_on('clicperformance', when="@0.1")
    depends_on('fcalclusterer', when="@0.1")
    depends_on('garlic', when="@0.1")
    depends_on('kaltest', when="@0.1")
    depends_on('lccd', when="@0.1")
    depends_on('marlindd4hep', when="@0.1")
    depends_on('marlinreco', when="@0.1")
    depends_on('clupatra', when="@0.1")
    depends_on('ddkaltest', when="@0.1")
    depends_on('gear', when="@0.1")
    depends_on('ilcutil', when="@0.1")
    depends_on('lcfiplus', when="@0.1")
    depends_on('lctuple', when="@0.1")
    depends_on('marlinfastjet', when="@0.1")
    depends_on('marlintrk', when="@0.1")
    depends_on('overlay', when="@0.1")
    depends_on('raida', when="@0.1")
    depends_on('ced', when="@0.1")
    depends_on('ddmarlinpandora', when="@0.1")
    depends_on('generalbrokenlines', when="@0.1")
    depends_on('ildperformance', when="@0.1")
    depends_on('kitrack', when="@0.1")
    depends_on('lcfivertex', when="@0.1")
    depends_on('lich', when="@0.1")
    depends_on('marlinkinfit', when="@0.1")
    depends_on('marlintrkprocessors', when="@0.1")
    depends_on('pandoraanalysis', when="@0.1")
    depends_on('sio', when="@0.1")



    depends_on("fccsw", when='@0.1')
    depends_on("podio@0.12.0", when="@0.1")

    # be explicit to avoid concretizer errors
    depends_on('root cxxstd=17 +root7 +ssl')
    depends_on('boost +python')

    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    
