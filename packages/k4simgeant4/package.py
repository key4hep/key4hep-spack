
from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage, k4_add_latest_commit_as_version 

class K4simgeant4(CMakePackage, Key4hepPackage):
    """Geant4 components of the Key4HEP software """
    homepage = "https://github.com/HEP-FCC/k4SimGeant4/"
    url      = "https://github.com/HEP-FCC/k4SimGeant4/archive/v0.1.0pre05.tar.gz"
    git      = "https://github.com/HEP-FCC/k4SimGeant4.git"

    maintainers = ['vvolkl']

    version('main', branch='main')
    version("0.1.0pre08", tag="v0.1.0pre08")

    variant('cxxstd',
            default='17',
            values=('14', '17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('k4fwcore@1.0:')
    depends_on('geant4')
    depends_on('edm4hep')
    depends_on("g4ensdfstate")


    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.set("K4SIMGEANT4", self.prefix.share.k4SimGeant4)
        install_path = join_path(self.spec['g4ensdfstate'].prefix.share,
                                 'data', 'G4ENSDFSTATE{0}'
                                 .format(self.spec['g4ensdfstate'].version))
        spack_env.set('G4ENSDFSTATEDATA', install_path)

    def setup_build_environment(self, spack_env):
        install_path = join_path(self.spec['g4ensdfstate'].prefix.share,
                                 'data', 'G4ENSDFSTATE{0}'
                                 .format(self.spec['g4ensdfstate'].version))
        spack_env.set('G4ENSDFSTATEDATA', install_path)

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib64)
