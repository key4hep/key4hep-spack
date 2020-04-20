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
    depends_on('dd4hep@master', when='@nightly')
    
    depends_on("edm4hep@0.1.0", when="@0.1")
    depends_on("K4FWCore@0.1.0", when="@0.1")
    depends_on('guinea-pig@1.2.2rc', when="@0.1")
    
