from spack import *
import sys 

class Cppunit(Package):
    """FIXME: put a proper description of your package here."""
    homepage = "http://www.example.com"
    url      = "http://downloads.sourceforge.net/project/cppunit/cppunit/1.12.1/cppunit-1.12.1.tar.gz"

    version('1.12.1', 'bd30e9cf5523cdfc019b94f5e1d7fd19')

    def install(self, spec, prefix):
        if sys.platform == 'darwin':
            perl=which('perl')
            perl('-p','-i.bak','-e','s|rm(.*)conftest|rm -fr $1 conftest|g', 'configure','aclocal.m4','libtool','config/ltmain.sh')


        import os
        os.environ["LDFLAGS"] = os.environ.get("LDFLAG", "") + " -ldl "
        configure('--prefix=%s' % prefix)

        make()
        make("install")
