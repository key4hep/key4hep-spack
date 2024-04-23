from spack.pkg.k4.key4hep_stack import Ilcsoftpackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests

class K4reco(CMakePackage, Ilcsoftpackage):
    """Reconstruction algorithms using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4Reco"
    url = "https://github.com/key4hep/k4Reco/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4Reco.git"

    version("master", branch="main")

    depends_on("root")
    depends_on("edm4hep")
    depends_on("k4fwcore")
    depends_on("gaudi")
    depends_on("dd4hep")
    depends_on("lcio")
    depends_on("k4simgeant4")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            )
        )
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        # needed to set up the runtime dependencies for tests
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib64)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib64)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib64)
        # k4_setup_env_for_framework_tests(self.spec, env)
