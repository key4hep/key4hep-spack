# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install gccxml
#
# You can always get back here to change things with:
#
#     spack edit gccxml
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Gccxml(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.gccxml.org/files/v0.6/gccxml-0.6.0.tar.gz"

    version('20150423', git='https://github.com/gccxml/gccxml.git',
        commit='3afa8ba5be6866e603dcabe80aff79856b558e24')
    version('0.6.0', 'd828349c76ca055955d0af84e8381093')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        cmake('.', *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
