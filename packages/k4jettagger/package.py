from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Fccanalyses(CMakePackage, Key4hepPackage):
    """RDF Analysers for the FCC."""

    homepage = "https://github.com/saracreates/JetTagging"
    git = "https://github.com/saracreates/JetTagging.git"
    # url = "https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    generator = "Ninja"

    depends_on("ninja", type="build")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("py-onnxruntime")

    def cmake_args(self):
        args = [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define("BUILD_TESTING", self.run_tests),
        ]

        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
