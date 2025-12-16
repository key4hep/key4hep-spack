from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4reco(CMakePackage, Key4hepPackage):
    """Reconstruction algorithms using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4Reco"
    url = "https://github.com/key4hep/k4Reco/archive/v00-01-00.tar.gz"
    git = "https://github.com/key4hep/k4Reco.git"

    version("main", branch="main")

    version(
        "0.3.0",
        sha256="a54074046631e935f792fcf6d4e1904c60c71bef8886217b35b46261631314dd",
    )
    version(
        "0.2.1",
        sha256="4d456945b31569f070806c7e40f3dcf01931af5d970f2f371597bfbe1b79cfd3",
    )
    version(
        "0.2.0",
        sha256="52b9459c000cc10583712670d668f15910e19587b614c922b52c9a593907c9ed",
    )
    version(
        "0.1.0",
        sha256="6309de6cb083f1d263c40b99f06b47b774d485dc5361f98dad2f6e111376d69e",
    )

    variant("conformal_tracking", default=True, description="Build Conformal Tracking")

    depends_on("cxx", type="build")

    depends_on("podio")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4fwcore@1.4:", when="@0.3.0:")
    depends_on("k4simgeant4")
    depends_on("root")

    depends_on("lcio", when="+conformal_tracking")
    depends_on("ilcutil", when="+conformal_tracking")
    depends_on("kaltest", when="+conformal_tracking")
    depends_on("ddkaltest", when="+conformal_tracking")

    depends_on("k4geo", type="test")

    def cmake_args(self):
        args = [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
            self.define_from_variant("BUILD_TRACKING", "conformal_tracking"),
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
