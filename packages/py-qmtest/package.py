# To install:
#
#     spack install py-qmtest
#
# You can always get back here to change things with:
#
#     spack edit py-qmtest
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class PyQmtest(Package):
    """ QmTest tes package for python."""
    homepage = "http://legacy.python.org/workshops/2002-02/papers/01/index.htm"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/qmtest-2.4.1.tar.gz"

    version('2.4.1', '860d4795351453013c9aaab246fd93ba')
    version('2.4'  , 'b1c7cd4aa78a0fda1a6598ece98f6033')

    depends_on("python")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)

