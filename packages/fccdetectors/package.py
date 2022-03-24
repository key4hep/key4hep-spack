
from spack.pkg.k4.key4hep_stack import Key4hepPackage 

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

    depends_on('dd4hep')
    depends_on('lcgeo')
    depends_on('lcio')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
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
