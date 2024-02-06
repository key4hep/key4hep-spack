from spack.pkg.k4.key4hep_stack import Ilcsoftpackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4fwcore(CMakePackage, Ilcsoftpackage):
    """Core framework components of the Key4HEP project"""

    homepage = "https://github.com/key4hep/k4FWCore"
    url = "https://github.com/key4hep/k4FWCore/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4FWCore.git"

    version("main", branch="main")
    version("1.0pre18", tag="v01-00pre18")
    version("1.0pre17", tag="v01-00pre17")
    version("1.0pre16", tag="v01-00pre16")
    version("1.0pre15", tag="v01-00pre15")
    version("1.0pre14", tag="v01-00pre14")
    version(
        "0.2.0",
        sha256="7d1a6e7494f08c2b25901cab2138795f21b6c4e84f05c4f8b9a6839787874b72",
    )
    version(
        "0.1.1",
        sha256="9c4e4b487f7d9c982547c13570345399505e763fb369b76ceadb35c1d52bf6aa",
    )
    version(
        "0.1.0",
        sha256="aef682649f3fcb1d72de897fbf6ec4ed421c8a4836bb3462c4b0049a709374e4",
    )

    patch(
        "https://github.com/key4hep/k4FWCore/commit/d1061e272a0688722e89491f5e5829dc9b352127.patch",
        when="@1.0pre14",
        sha256="da089b320d0bd89c5b6d8a972009e11f324a442e6bb85778d8541364f957b4f9",
    )

    depends_on("gaudi@35.0:", when="@0.3.0:")
    depends_on("gaudi@32.2:34.99", when="@:0.2.99")
    depends_on("root@6.08:")
    depends_on("podio@0.10:")
    depends_on("podio@0.14.1", when="@1.0pre14:1.0pre15")
    depends_on("podio@0.14.2:", when="@1.0pre16:")
    depends_on("podio@:0.17.3", when="@:1.0pre17")  # podio/EventStore.h removed
    depends_on("edm4hep")
    depends_on("edm4hep@0.4.1:", when="@1.0pre14:")
    depends_on("edm4hep@0.10.2:", when="@1.0pre17:")
    # needed via gaudi
    depends_on("py-six", type=("build", "run"))

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            )
        )
        # Setting this bypasses the get_binary_tag.py script
        # and a check for BINARY_TAG which is not used in this build system
        # should become obsolete with the cmake modernisation in gaudi v34
        if self.spec.satisfies("^gaudi@:34.99"):
            args.append("-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt")
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        # needed to set up the runtime dependencies for tests
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib64)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib64)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib64)
        # k4_setup_env_for_framework_tests(self.spec, env)
