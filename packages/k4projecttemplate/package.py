from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4projecttemplate(CMakePackage, Key4hepPackage):
    """Template for Key4hep framework projects"""

    homepage = "https://github.com/key4hep/k4-project-template/"
    url = (
        "https://github.com/key4hep/k4-project-template/archive/refs/tags/v0.2.0.tar.gz"
    )
    git = "https://github.com/key4hep/k4-project-template.git"

    maintainers("vvolkl")

    version("main", branch="main")
    version(
        "0.5.0",
        sha256="801ecc3319109c74ba62decd57473be8c65aea79991b7c4ac5e5a84209036f9a",
    )
    version(
        "0.4.1",
        sha256="02a6432e7661a16371bda87d4352cd92bc77168a7f28528353ade721e931984c",
    )
    version(
        "0.4.0",
        sha256="e1fb8992f85ba29918e1103d3472e4ca272a16b09819f7d1ed79e6d97c4445a4",
    )

    generator = "Ninja"

    depends_on("ninja", type="build")
    depends_on("edm4hep")
    depends_on("k4fwcore@1.0pre14:", when="@0.3.0:")
    depends_on("k4fwcore@1:")
    depends_on("root")

    def cmake_args(self):
        args = [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.set("K4PROJECTTEMPLATE", self.prefix.share.k4ProjectTemplate)
