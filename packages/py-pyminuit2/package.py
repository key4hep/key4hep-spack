# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install py-pyminuit2
#
# You can always get back here to change things with:
#
#     spack edit py-pyminuit2
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class PyPyminuit2(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/pyminuit2-0.0.1.tar.gz"

    version('0.0.1', '9035b9ab03cba2b31ce6f75f37585112')

    # FIXME: Add dependencies if this package requires them.
    depends_on("root")
    depends_on("py-setuptools")
    extends("python")    

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        python('setup.py', 'install', '--prefix=%s' % prefix)
