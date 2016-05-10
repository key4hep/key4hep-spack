# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install py-coverage
#
# You can always get back here to change things with:
#
#     spack edit py-coverage
#
# See the spack documentation for more information on building
# packages.
#
from spack import *



class PyCoverage(Package):
    """code coverage on Python"""
    homepage = "http://nedbatchelder.com/code/coverage/"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/coverage-3.5.2.tar.gz"

    version('3.5.2', '28c43d41b13f8987ea14d7b1d4a4e3ec')

    depends_on("py-setuptools")
    extends("python")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
