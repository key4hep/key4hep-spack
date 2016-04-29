from spack import *
import os
import glob

class Aida(Package):
    """AIDA Headers."""
    homepage = "http://www.example.com"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/aida-3.2.1-src.tar.gz"

    version('3.2.1', 'c35073da04abfdd96ac9f4801f3da473')

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        cp = which('cp')
        cp('-r', 'src/cpp/AIDA', prefix + '/include')
