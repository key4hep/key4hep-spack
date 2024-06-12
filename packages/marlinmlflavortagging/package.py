#!/usr/bin/env python3

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinmlflavortagging(CMakePackage, Ilcsoftpackage):
    """Package with processors for running deep ML based flavor taggers in Marlin."""

    homepage = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging"
    git = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging.git"
    url = "https://gitlab.desy.de/ilcsoft/MarlinMLFlavorTagging"

    maintainers("tmadlener")

    version("main", branch="main")

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
