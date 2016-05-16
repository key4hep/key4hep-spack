# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install heppdt
#
# You can always get back here to change things with:
#
#     spack edit heppdt
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Heppdt(Package):
    """ HEPPDT ."""
    homepage = "http://lcgapp.cern.ch/project/simu/HepPDT/"
    url      = "http://lcgapp.cern.ch/project/simu/HepPDT/download/HepPDT-2.06.01.tar.gz"

    version('3.04.01', 'a8e93c7603d844266b62d6f189f0ac7e')
    version('3.04.00', '2d2cd7552d3e9539148febacc6287db2')
    version('3.03.02', '0b85f1809bb8b0b28a46f23c718b2773')
    version('3.03.01', 'd411f3bfdf9c4350d802241ba2629cc2')
    version('3.03.00', 'cd84d0a0454be982dcd8c285e060a7b3')
    version('2.06.01', '5688b4bdbd84b48ed5dd2545a3dc33c0')

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)

        make()
        make("install")
