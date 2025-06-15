from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4mljettagger(CMakePackage, Key4hepPackage):
    """Implementation of Jet-Flavor Tagging on CLD full simulation with the ParticleTransformer"""

    homepage = "https://github.com/key4hep/k4MLJetTagger"
    git = "https://github.com/key4hep/k4MLJetTagger.git"
    url = "https://github.com/key4hep/archive/v0.1.0.tar.gz"

    maintainers("jmcarcell")

    version("main", branch="main")
    version(
        "0.1.0",
        sha256="175bcc75bf6378880aa8fc85a1a1e3f75b400633c9ec88e0583431e085451463",
    )

    generator = "Ninja"

    depends_on("c", type="build")
    depends_on("cxx", type="build")

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
