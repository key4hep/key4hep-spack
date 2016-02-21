from spack import *

class Lcov(Package):
    """
    LCOV is a graphical front-end for GCC's coverage testing tool gcov.
    """

    homepage = "http://ltp.sourceforge.net/coverage/lcov.php"
    url      = "http://downloads.sourceforge.net/ltp/lcov-1.12.tar.gz"

    version('1.12', 'e497f9b77a93c6dda4e594cd8a67f634')

    def install(self, spec, prefix):
        make()
        make("install",'PREFIX=%s' % prefix)
