
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class Fccdetectors(CMakePackage, Key4hepPackage):
    """Software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/fccDetectors/"
    url      = "https://github.com/HEP-FCC/fccDetectors/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/fccDetectors.git"

    maintainers = ['vvolkl']

    version('main', branch='main')
    # can be removed once the ci is fixed
    version('master', branch='main')
    version("0.1pre04", tag="v0.1pre04")


    variant('cxxstd',
            default='17',
            values=('14', '17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('dd4hep +geant4')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)

    def test(self):
        self.run_test('geoDisplay', options=["$FCCDETECTORS/Detector/DetFCChhBaseline1/compact/FCChh_DectMaster.xml"], purpose="Construct FCChh Detector Geometry.")
