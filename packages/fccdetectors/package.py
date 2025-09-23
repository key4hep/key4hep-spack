from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Fccdetectors(CMakePackage, Key4hepPackage):
    """FCC Detector Descriptions"""

    homepage = "https://github.com/HEP-FCC/FCCDetectors/"
    url = "https://github.com/HEP-FCC/FCCDetectors/archive/refs/tags/v0.1pre03.tar.gz"
    git = "https://github.com/HEP-FCC/FCCDetectors.git"

    maintainers("vvolkl")

    version("main", branch="main")
    version("0.1pre11", tag="v0.1pre11")
    version("0.1pre10", tag="v0.1pre10")
    version("0.1pre09", tag="v0.1pre09")
    version("0.1pre08", tag="v0.1pre08")
    version("0.1pre07", tag="v0.1pre07")
    version("0.1pre06", tag="v0.1pre06")

    depends_on("cxx", type="build")

    depends_on("dd4hep")
    depends_on("k4geo")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
            "-DCMAKE_INSTALL_LIBDIR=lib"
        )
        return args

    def setup_run_environment(self, env):
        env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("FCCDETECTORS", self.prefix.share.FCCDetectors)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def test(self):
        self.run_test(
            "geoDisplay",
            options=[
                "$FCCDETECTORS/Detector/DetFCChhBaseline1/compact/FCChh_DectMaster.xml"
            ],
            purpose="Construct FCChh Detector Geometry.",
        )
