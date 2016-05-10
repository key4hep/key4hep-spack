# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install py-matplotlib
#
# You can always get back here to change things with:
#
#     spack edit py-matplotlib
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class PyMatplotlib(Package):
    """a python 2D plotting library"""
    homepage = "http://matplotlib.sourceforge.net/"
    url      = "http://service-spi.web.cern.ch/service-spi/external/tarFiles/matplotlib-1.5.1.tar.gz"

    version('1.5.1', 'f51847d8692cb63df64cd0bd0304fd20')
    version('1.4.3', '86af2e3e3c61849ac7576a6f5ca44267')
    version('1.3.1', '444624ad58de05f9029b0b5811e11c17')
    version('1.1.0', '57a627f30b3b27821f808659889514c2')

    depends_on("py-setuptools")
    depends_on("py-numpy")
    depends_on("py-nose")
    depends_on("py-pyparsing")
    depends_on("py-pytz")
    depends_on("py-mock")
    depends_on("freetype")
    extends("python")


    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
