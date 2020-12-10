
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class K4gen(CMakePackage, Key4hepPackage):
    """Generator components for the Key4hep framework"""
    homepage = "https://github.com/HEP-FCC/k4Gen/"
    url      = "https://github.com/HEP-FCC/k4Gen/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/k4Gen.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.1pre01', tag='0.1pre01')

    generator = 'Ninja'

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('ninja', type='build')
    depends_on('fastjet')
    depends_on("edm4hep")
    depends_on('k4fwcore@1:')
    depends_on('hepmc@:2.99.99')
    depends_on('heppdt@:2.99.99')
    depends_on('pythia8')
    depends_on('evtgen+pythia8')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.set("K4GEN", self.prefix.share.k4Gen)
