from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4actstracking(CMakePackage, Key4hepPackage):
    """Acts tracking components for the key4hep project"""

    homepage = "https://github.com/key4hep/k4ActsTracking"
    # todo
    # url = "https://github.com/key4hep/k4ActsTracking"
    git = "https://github.com/key4hep/k4ActsTracking.git"

    maintainers("vvolkl")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("acts+dd4hep+tgeo+json")
    depends_on("gaudi")
    depends_on("root")
    depends_on("edm4hep")
    depends_on("k4fwcore")

    def cmake_args(self):
        return []
