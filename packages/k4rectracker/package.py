from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4rectracker(CMakePackage, Key4hepPackage):
    """Tracking detectors (and similar) digitization and reconstruction using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4RecTracker"
    url = "https://github.com/key4hep/k4RecTracker/archive/refs/tags/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4RecTracker.git"

    version("master", branch="master")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("marlinutil")
    depends_on("root")
    # This shouldn't be necessary but the debug builds are failing because lcio can't be found
    # It started happening after adding marlinutil to the dependencies
    depends_on("lcio")

    def cmake_args(self):
        args = []
        args.append(
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            )
        )
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4rectracker"].prefix.lib)
