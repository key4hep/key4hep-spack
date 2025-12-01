from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4actstracking(CMakePackage, Key4hepPackage):
    """Acts tracking components for the key4hep project"""

    homepage = "https://github.com/key4hep/k4ActsTracking"
    # todo
    url = "https://github.com/key4hep/k4ActsTracking/archive/refs/tags/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4ActsTracking.git"

    maintainers("vvolkl")

    version("main", branch="main")
    version(
        "00-01",
        sha256="05901153900064673417b559d4a4a5d9ebc6e783367130a5b20abe1c83bc39eb",
    )

    depends_on("cxx", type="build")

    depends_on("acts+dd4hep+tgeo+json")
    depends_on("gaudi")
    depends_on("root")
    depends_on("edm4hep")
    depends_on("k4fwcore")
    depends_on("opendatadetector", type="test")

    def cmake_args(self):
        return []

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4reco"].prefix.lib)
