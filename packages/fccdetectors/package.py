
from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage, k4_add_latest_commit_as_version 

class Fccdetectors(CMakePackage, Key4hepPackage):
    """FCC Detector Descriptions"""
    homepage = "https://github.com/HEP-FCC/FCCDetectors/"
    url      = "https://github.com/HEP-FCC/FCCDetectors/archive/refs/tags/v0.1pre03.tar.gz"
    git      = "https://github.com/HEP-FCC/FCCDetectors.git"

    maintainers = ['vvolkl']

    version('main', branch='main')
    # can be removed once the ci is fixed
    version('master', branch='main')
    version("0.1pre06", tag="v0.1pre06")


    variant('cxxstd',
            default='17',
            values=('14', '17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('dd4hep +geant4')
    depends_on('lcgeo')
    depends_on('lcio')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')

    def setup_build_environment(self, spack_env):
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib64)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)

    def test(self):
        self.run_test('geoDisplay', options=["$FCCDETECTORS/Detector/DetFCChhBaseline1/compact/FCChh_DectMaster.xml"], purpose="Construct FCChh Detector Geometry.")
