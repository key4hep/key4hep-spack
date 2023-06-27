
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
    version("0.1pre09", tag="v0.1pre09")
    version("0.1pre08", tag="v0.1pre08")
    version("0.1pre07", tag="v0.1pre07")
    version("0.1pre06", tag="v0.1pre06")

    depends_on('dd4hep')
    depends_on('k4geo')
    depends_on('lcio')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
        return args

    def setup_run_environment(self, env):
        env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['k4geo'].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['k4geo'].prefix.lib64)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.spec['fccdetectors'].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['fccdetectors'].prefix.lib64)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec['k4geo'].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['k4geo'].prefix.lib64)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].libs.directories[0])

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib64)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def test(self):
        self.run_test('geoDisplay', options=["$FCCDETECTORS/Detector/DetFCChhBaseline1/compact/FCChh_DectMaster.xml"], purpose="Construct FCChh Detector Geometry.")
