from spack import *

class Gccxml(Package):
    """FIXME: put a proper description of your package here."""
    homepage = "http://www.example.com"
    url      = "http://www.gccxml.org/files/v0.6/gccxml-0.6.0.tar.gz"

    version('20150423', git='https://github.com/gccxml/gccxml.git',
        commit='3afa8ba5be6866e603dcabe80aff79856b558e24')
    version('0.6.0', 'd828349c76ca055955d0af84e8381093')

    depends_on('cmake', type='build')

    def install(self, spec, prefix):
        cmake('.', *std_cmake_args)

        make()
        make("install")
