
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version

class K4lcioreader(CMakePackage, Key4hepPackage):
    """LCIO reader based on PODIO and EDM4hep"""
    homepage = "https://github.com/key4hep/k4LCIOReader"
    url      = "https://github.com/key4hep/k4LCIOReader/archive/v0.1.0.tar.gz"
    git      = "https://github.com/key4hep/k4LCIOReader.git"

    maintainers = ['mirguest']

    version('master', branch='master')
    version('0.3.2', sha256='dac76172d484faa23ca170fc89b4cfec6ce56777cd0c20b2b608838824582447')
    version('0.3.1', sha256='cb7614db76972f8b22ccb69cfaa19931b8fdb60f8a506d2b8ff524dd6fcbf0a9')
    version('0.3.0', sha256='ce6a5596a21bfa23e641eda84830d8aa7caf15fd47da35878ee61e7f555d0e51')
    version('0.2.0', sha256='346fc2ba4b4175895597e093f566ba6407be9eeb9cde0766304e0f19ad03e081')
    version('0.1.0', sha256='996d1ff78c0a8a2f7f358dd4ea19f955853ad0902ee86b99c484de58c5fc2e2c')

    variant('cxxstd',
            default='17',
            values=('14', '17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')


    depends_on('lcio')
    depends_on('podio@0.12:')
    depends_on('edm4hep')
    depends_on('k4fwcore@0.2.0', when='@:0.2.0')
    depends_on('k4fwcore@0.3.0:', when='@0.3:')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        return args
