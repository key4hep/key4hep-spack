from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4pfhitml(CMakePackage, Key4hepPackage):
    """Machine learning particle flow reconstruction from calorimeter hits."""

    homepage = "https://github.com/key4hep/k4PFHitML"
    git = "https://github.com/key4hep/k4PFHitML.git"
    url = "https://github.com/key4hep/k4PFHitML/archive/refs/tags/v00-02.tar.gz"

    maintainers("jmcarcell")

    version("main", branch="main")
    version(
        "00-02",
        sha256="3429dc8d49a735aa56d3e4c9cbaed66a7f824b2f3e465fcf52084dc7d0c117d4",
    )

    depends_on("cxx", type="build")

    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("py-onnxruntime")
    depends_on("py-torch")
    depends_on("root")

    def cmake_args(self):
        return [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
