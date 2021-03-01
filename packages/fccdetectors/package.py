
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class Fccdetectors(CMakePackage, Key4hepPackage):
    """Software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/fccDetectors/"
    url      = "https://github.com/HEP-FCC/fccDetectors/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/fccDetectors.git"

    maintainers = ['vvolkl']

    version('main', branch='main')
    version("0.1pre01", tag="v0.1pre01")

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('dd4hep +geant4')
    depends_on('edm4hep')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("FCCDETECTORS", self.prefix.share.fccDetectors)
