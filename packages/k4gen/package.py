from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4gen(CMakePackage, Key4hepPackage):
    """Generator components for the Key4hep framework"""

    homepage = "https://github.com/HEP-FCC/k4Gen/"
    url = "https://github.com/HEP-FCC/k4Gen/archive/refs/tags/v0.1pre02.tar.gz"
    git = "https://github.com/HEP-FCC/k4Gen.git"

    maintainers = ["vvolkl"]

    version("main", branch="main")
    version(
        "0.1pre10",
        sha256="803a796fa9a7fe43a04dfac95fa9143cb275796194012d5b283e062b4a7b8a12",
    )
    version("0.1pre09", tag="v0.1pre09")
    version("0.1pre08", tag="v0.1pre08")
    version("0.1pre07", tag="v0.1pre07")
    version("0.1pre06", tag="v0.1pre06")
    version("0.1pre05", tag="v0.1pre05")

    generator = "Ninja"

    depends_on("ninja", type="build")
    depends_on("fastjet")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("k4fwcore@1.0pre14:", when="@0.1pre06:")
    depends_on("k4fwcore@1:")
    depends_on("hepmc@:2.99.99", when="@:0.1pre05")
    depends_on("hepmc3")
    depends_on("heppdt@:2.99.99")
    depends_on("pythia8")
    depends_on("evtgen+pythia8")
    depends_on("root")
    depends_on("py-six", type=("build", "run"))

    # Temporary patch to allow C++20
    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/k4Gen/pull/26.diff",
        sha256="9f8572eabd2f230d373801482349371873301e4d2efd017bdfea4631a5aeba43",
    )

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib64)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib64)
        env.set("K4GEN", self.prefix.share.k4Gen)

    def setup_build_environment(self, env):
        # k4_setup_env_for_framework_tests(self.spec, env)
        env.set("K4GEN", self.prefix.share.k4Gen)
        # todo: workaround, fix properly in cmake
        env.prepend_path("CPATH", self.spec["heppdt"].prefix.include)

    def check(self):
        pass

    # ... and  add custom check step that runs after installation instead
    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
