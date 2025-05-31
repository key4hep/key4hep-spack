from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class K4fwcore(CMakePackage, Ilcsoftpackage):
    """Core framework components of the Key4HEP project"""

    homepage = "https://github.com/key4hep/k4FWCore"
    url = "https://github.com/key4hep/k4FWCore/archive/v00-01-00.tar.gz"
    git = "https://github.com/key4hep/k4FWCore.git"

    version("main", branch="main")

    version(
        "1.3",
        sha256="3a484594b4f101a3b4755ca7ee71458440b5edfd5b455b7e64176ad6f0025d01",
    )
    version(
        "1.2",
        sha256="4405a3d6e88845807d57849a759827ad988681c31c9e63851b9f7d30c9a407e4",
    )
    version(
        "1.1.2",
        sha256="5451f1644357ac8ced0f5fc984809f4a48bdf2f4baf25a0a2f70540ed0427ac4",
    )
    version(
        "1.1.1",
        sha256="8ae8dc54e50c26537ac94050e08c4ad6c80e1555abd7bfd0e242d04c93e6017c",
    )
    version(
        "1.1",
        sha256="63a81e5893571a5e9209e4b6f2fe6d511772675a824cfef105f2df5f18fc6af4",
    )

    version("1.0pre19", tag="v01-00pre19")
    version("1.0pre18", tag="v01-00pre18")
    version("1.0pre17", tag="v01-00pre17")
    version("1.0pre16", tag="v01-00pre16")

    depends_on("cxx", type="build")

    depends_on("gaudi")
    depends_on("gaudi +gaudialg", when="@:1.0pre19 ^gaudi@37:")
    depends_on("root")
    depends_on("podio")
    depends_on("podio@1.0.1:", when="@1.1:")  # linking against podioIO
    depends_on("podio@:0.17.3", when="@:1.0pre17")  # podio/EventStore.h removed
    depends_on("edm4hep")
    depends_on("edm4hep@0.10.2:", when="@1.0pre17:")

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
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib64)
