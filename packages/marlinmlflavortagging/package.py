from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Marlinmlflavortagging(CMakePackage, Key4hepPackage):
    """Package with processors for running deep ML based flavor taggers in Marlin."""

    homepage = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging"
    git = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging.git"
    url = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging/-/archive/v0.1.0/MarlinMLFlavorTagging-v0.1.0.tar.gz"

    maintainers("tmadlener")

    version("main", branch="main")
    version(
        "0.1.0",
        sha256="4ad9193e433fc7d06f53941b982a52f257f13bdfc882100ed42d6c7ca8689a20",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("aida")
    depends_on("ilcutil")
    depends_on("lcio@2.21:")
    depends_on("lcfivertex")
    depends_on("marlin@1.17: +aida")
    depends_on("root")
    depends_on("py-torch")

    @property
    def libs(self):
        # Make the library that should go on MARLIN_DLL available via this
        # property by explicitly finding it (also takes care of lib vs lib64)
        return find_libraries(
            "libMarlinMLFlavorTagging", root=self.prefix, recursive=True, shared=True
        )

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.libs.libraries[0])
