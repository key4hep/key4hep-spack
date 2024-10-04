from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class K4fwcore(CMakePackage, Ilcsoftpackage):
    """Core framework components of the Key4HEP project"""

    homepage = "https://github.com/key4hep/k4FWCore"
    url = "https://github.com/key4hep/k4FWCore/archive/v00-01-00.tar.gz"
    git = "https://github.com/key4hep/k4FWCore.git"

    version("main", branch="main")

    version(
        "1.1.0",
        sha256="31b03daf5f839708113f3452c6626975aa8b070a7cbbb3576b29b86918df13d3",
    )

    version("1.0pre19", tag="v01-00pre19")
    version("1.0pre18", tag="v01-00pre18")
    version("1.0pre17", tag="v01-00pre17")
    version("1.0pre16", tag="v01-00pre16")
    version("1.0pre15", tag="v01-00pre15")
    version("1.0pre14", tag="v01-00pre14")

    patch(
        "https://github.com/key4hep/k4FWCore/commit/d1061e272a0688722e89491f5e5829dc9b352127.patch",
        when="@1.0pre14",
        sha256="da089b320d0bd89c5b6d8a972009e11f324a442e6bb85778d8541364f957b4f9",
    )

    depends_on("gaudi")
    depends_on("gaudi +gaudialg", when="@:1.0pre19 ^gaudi@37:")
    depends_on("root")
    depends_on("podio")
    depends_on("podio@0.14.1", when="@1.0pre14:1.0pre15")
    depends_on("podio@0.14.2:", when="@1.0pre16:")
    depends_on("podio@:0.17.3", when="@:1.0pre17")  # podio/EventStore.h removed
    depends_on("edm4hep")
    depends_on("edm4hep@0.4.1:", when="@1.0pre14:")
    depends_on("edm4hep@0.10.2:", when="@1.0pre17:")

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
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["gaudi"].prefix.lib64)
