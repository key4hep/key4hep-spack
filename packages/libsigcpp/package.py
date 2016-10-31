from spack import *

class Libsigcpp(Package):
    """Description"""

    homepage = "http://www.example.com"
    url      = "http://home.fnal.gov/~gartung/spack_mirror/libsigcpp/libsigcpp-2.6.2.tar.gz"

    version('2.6.2', 'a16911fcd894d7e43e73fc5e8751f3fe')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
