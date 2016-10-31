from spack import *

class PyPyminuit2(Package):
    """FIXME: put a proper description of your package here."""
    homepage = "http://www.example.com"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/pyminuit2-0.0.1.tar.gz"

    version('0.0.1', '9035b9ab03cba2b31ce6f75f37585112')

    depends_on("root")
    depends_on("py-setuptools")
    extends("python")    

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
