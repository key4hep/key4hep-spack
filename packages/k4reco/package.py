from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4reco(CMakePackage, Key4hepPackage):
    """Reconstruction algorithms using Gaudi in native key4hep"""

    homepage = "https://github.com/key4hep/k4Reco"
    url = "https://github.com/key4hep/k4Reco/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4Reco.git"

    version("main", branch="main")

    version(
        "0.1.0",
        sha256="93ee8a66aeb31ed501a356a145551f9836fb744e22b435c6577ea5274ece39c6",
    )

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4simgeant4")
    depends_on("root")

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
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
