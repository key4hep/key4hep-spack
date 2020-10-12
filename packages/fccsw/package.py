
from spack import *
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_version 

class Fccsw(CMakePackage):
    """software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.5.tar.gz"
    git      = "https://github.com/HEP-FCC/FCCSW.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.13', sha256='4b76b28404f02dac09d9b02eb1db9926f5a53b21c6b91e95d3812267d575b116')
    version('0.12', sha256='a67151c12177882abd8afcf56bee47c2830c44cac749b23d08d005b45096b264')
    version('0.11', 'e3b5aa8f396cffae745305801eb8f7a38a8a7881')
    version('0.10', '40b75f42fb51934cdc3c52049226ac39')
    version('0.9', 'fbbfc1deeaab40757d05ebfcbfa7b0f5')
    version('0.5.1', 'e2e6e6fa40373c3a14ea823bb9bc0810')
    version('0.5', 'f2c849608ac1ab175f432a5e55dbe673')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('acts', when='@0.15:')
    depends_on('acts@0.10.5 +identification +dd4hep +tgeo +digitization', when="@0.12:0.14")
    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('delphes@3.4.3pre05:', when="@0.15:")
    depends_on('delphes')
    depends_on('eigen')
    depends_on('fastjet')

    depends_on('fcc-edm@0.5.5', when="@:0.12")
    depends_on('fcc-edm@0.5.7:', when="@0.13:")

    depends_on('gaudi', when="@0.13:")
    depends_on('gaudi@32.2', when="@:0.12")
    depends_on('geant4', when='@0.13:')
    depends_on('geant4@10.6.1', when='@:0.12')
    depends_on('hepmc@:2.99.99')
    depends_on('heppdt@:2.99.99')

    depends_on('papas', when="@:0.12")

    depends_on('podio@0.9.2', when="@:0.12")
    depends_on('podio@0.10.0:', when="@0.13:")
    depends_on('pythia8', when="@:0.12")
    depends_on('evtgen+pythia8', when="@0.13:")
    depends_on('root')


    depends_on("k4fwcore", when="@0.13:")
    depends_on("edm4hep", when="@0.13:")

    depends_on("g4ensdfstate")




    patch('permissions.patch', when='@0.9')
    patch('ddeve.patch', when='@0.9 ^dd4hep@01-08')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
          args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

    def setup_build_environment(self, spack_env):
        spack_env.set('G4ENSDFSTATEDATA', self.spec["g4ensdfstate"].prefix + "/share/data/G4ENSDFSTATE2.2/")

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.set_path("FCCSWBASEDIR", self.prefix)
        spack_env.set_path("FCC_DETECTORS", self.prefix.share.FCCSW)
        spack_env.set_path("FCCSW", self.prefix.share.FCCSW)
