from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4reccalorimeter(CMakePackage, Key4hepPackage):
    """Calorimeter reconstruction components for the Key4hep framework"""

    homepage = "https://github.com/HEP-FCC/k4RecCalorimeter/"
    url = "https://github.com/HEP-FCC/k4RecCalorimeter/archive/refs/tags/v0.1.0pre04.tar.gz"
    git = "https://github.com/HEP-FCC/k4RecCalorimeter.git"

    maintainers("vvolkl")

    version("main", branch="main")
    version(
        "0.1.0pre17",
        sha256="7e8d73e107d0d715f40a1277e97e0f14f8b5f3ad4dd0c75fc3a52fc1b5c641c2",
    )
    version(
        "0.1.0pre16",
        sha256="a7c1a92a6bf5d641ddf797d3f8b8d1cb90c8a866956a15fd5dd27ff984755b74",
    )
    version(
        "0.1.0pre15",
        sha256="8406e7ca3ff78a93ace7ca645f49bea979931b9f268e5d2aaad958886f9e7b55",
    )
    version(
        "0.1.0pre14",
        sha256="4e3480e02806a708fabcb4014f082e1de89cb4a2fb838994848bef6664ff5168",
    )
    version("0.1.0pre13", tag="v0.1.0pre13")
    version("0.1.0pre12", tag="v0.1.0pre12")
    version("0.1.0pre11", tag="v0.1.0pre11")

    generator = "Ninja"

    depends_on("cxx", type="build")

    depends_on("ninja", type="build")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("fastjet")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4geo")
    depends_on("k4simgeant4")
    depends_on("podio")
    depends_on("py-onnxruntime")
    depends_on("root")
    depends_on("simsipm")

    def cmake_args(self):
        args = []
        args.extend(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            "-DCMAKE_INSTALL_LIBDIR=lib",
        )
        return args

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reccalorimeter"].prefix.lib)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.set("K4RECCALORIMETER", self.prefix.share.k4RecCalorimeter)

    def setup_build_environment(self, env):
        self.setup_run_environment(env)

    def check(self):
        pass

    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
