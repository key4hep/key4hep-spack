from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4reco(CMakePackage, Key4hepPackage):
    """Reconstruction algorithms using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4Reco"
    url = "https://github.com/key4hep/k4Reco/archive/v00-01-00.tar.gz"
    git = "https://github.com/key4hep/k4Reco.git"

    version("main", branch="main")

    version(
        "0.1.0",
        sha256="6309de6cb083f1d263c40b99f06b47b774d485dc5361f98dad2f6e111376d69e",
    )

    variant("conformal_tracking", default=True, description="Build Conformal Tracking")

    depends_on("podio")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4simgeant4")
    depends_on("root")

    depends_on("lcio", when="+conformal_tracking")
    depends_on("ilcutils", when="+conformal_tracking")
    depends_on("kaltest", when="+conformal_tracking")
    depends_on("ddkaltest", when="+conformal_tracking")

    def cmake_args(self):
        args = [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
            self.define_from_variant("BUILD_TRACKING", "conformal_tracking"),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
