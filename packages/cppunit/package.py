from spack import *

class Cppunit(Package):
    """FIXME: put a proper description of your package here."""
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/cppunit/cppunit/1.12.1/cppunit-1.12.1.tar.gz"

    version('1.12.1', 'bd30e9cf5523cdfc019b94f5e1d7fd19')

    def install(self, spec, prefix):
        import os
        os.environ["LDFLAGS"] = os.environ.get("LDFLAG", "") + " -ldl "
        configure('--prefix=%s' % prefix)

        make()
        make("install")
