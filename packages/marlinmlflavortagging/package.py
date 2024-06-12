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

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.libs.directories[0])
