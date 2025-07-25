from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4gen(CMakePackage, Key4hepPackage):
    """Generator components for the Key4hep framework"""

    homepage = "https://github.com/HEP-FCC/k4Gen/"
    url = "https://github.com/HEP-FCC/k4Gen/archive/refs/tags/v0.1pre02.tar.gz"
    git = "https://github.com/HEP-FCC/k4Gen.git"

    maintainers("vvolkl")

    version("main", branch="main")
    version(
        "0.1pre14",
        sha256="b52a68509336bd660953fc56fe6193439ecee76b9843153d5682a2ed77baf3ab",
    )
    version(
        "0.1pre13",
        sha256="d2a7fe39b1984325c7aeb5fdedbf46f1ae3c0a14c0105ad54a521b366c410c8e",
    )
    version(
        "0.1pre12",
        sha256="1356f748c0be4d5a33f0e1b2b3f4fbd9f03e185f1f53df2d59b254f960e860af",
    )
    version(
        "0.1pre11",
        sha256="750900ee2da2a09a101843e9ea03cc0cbd04451f3dbe01336c4adece06097efc",
    )
    version(
        "0.1pre10",
        sha256="803a796fa9a7fe43a04dfac95fa9143cb275796194012d5b283e062b4a7b8a12",
    )
    version("0.1pre09", tag="v0.1pre09")
    version("0.1pre08", tag="v0.1pre08")
    version("0.1pre07", tag="v0.1pre07")

    generator = "Ninja"

    depends_on("cxx", type="build")

    depends_on("ninja", type="build")
    depends_on("fastjet")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("k4fwcore")
    depends_on("hepmc3")
    depends_on("heppdt@:2.99.99")
    depends_on("pythia8")
    depends_on("evtgen+pythia8")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gen"].prefix.lib)
        env.set("K4GEN", self.prefix.share.k4Gen)

    def setup_build_environment(self, env):
        env.set("K4GEN", self.prefix.share.k4Gen)

    def check(self):
        pass

    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
