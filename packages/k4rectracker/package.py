from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4rectracker(CMakePackage, Key4hepPackage):
    """Tracking detectors (and similar) digitization and reconstruction using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4RecTracker"
    url = "https://github.com/key4hep/k4RecTracker/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/key4hep/k4RecTracker.git"

    version("master", branch="master")
    version(
        "0.5.0",
        sha256="82bc11059689676585a5494be86849b800ef86965485271c325ea4f3176caaac",
    )
    version(
        "0.4.0",
        sha256="c93d75df8d219d821617b9365ef3034aa5ba69617a626585f438f2f06bfa8e5f",
    )
    version(
        "0.3.0",
        sha256="e945be69b1b4d51b07e8e806e366893af84369a9d63b04deee691aa10d591a02",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("marlinutil")
    depends_on("root")
    depends_on(
        "delphes", when="@0.6.0:"
    )  # To be updated with specifc version once new delphes tag with latest changes is released
    # This shouldn't be necessary but the debug builds are failing because lcio can't be found
    # It started happening after adding marlinutil to the dependencies
    depends_on("lcio")
    depends_on("pandorasdk", when="@0.4.0:")

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value),
            self.define("BUILD_TESTING", self.run_tests), # not used in the package
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4rectracker"].prefix.lib)
