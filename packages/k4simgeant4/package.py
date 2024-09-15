from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4simgeant4(CMakePackage, Key4hepPackage):
    """Geant4 components of the Key4HEP software"""

    homepage = "https://github.com/HEP-FCC/k4SimGeant4/"
    url = "https://github.com/HEP-FCC/k4SimGeant4/archive/v0.1.0pre05.tar.gz"
    git = "https://github.com/HEP-FCC/k4SimGeant4.git"

    maintainers = ["vvolkl"]

    version("main", branch="main")
    version("0.1.0pre14", tag="v0.1.0pre14")
    version("0.1.0pre13", tag="v0.1.0pre13")
    version("0.1.0pre12", tag="v0.1.0pre12")
    version("0.1.0pre11", tag="v0.1.0pre11")
    version("0.1.0pre10", tag="v0.1.0pre10")
    version("0.1.0pre09", tag="v0.1.0pre09")
    version("0.1.0pre08", tag="v0.1.0pre08")

    depends_on("clhep")
    depends_on("dd4hep")
    depends_on("k4fwcore@1.0:")
    depends_on("geant4")
    depends_on("edm4hep")
    depends_on("g4ensdfstate")
    depends_on("root")
    # testing
    depends_on("fccdetectors")
    depends_on("k4gen")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.set("K4SIMGEANT4", self.prefix.share.k4SimGeant4)
        install_path = join_path(
            self.spec["g4ensdfstate"].prefix.share,
            "data",
            "G4ENSDFSTATE{0}".format(self.spec["g4ensdfstate"].version),
        )
        env.set("G4ENSDFSTATEDATA", install_path)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4simgeant4"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4simgeant4"].prefix.lib64)

    def setup_build_environment(self, env):
        install_path = join_path(
            self.spec["g4ensdfstate"].prefix.share,
            "data",
            "G4ENSDFSTATE{0}".format(self.spec["g4ensdfstate"].version),
        )
        env.set("G4ENSDFSTATEDATA", install_path)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4simgeant4"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4simgeant4"].prefix.lib64)
