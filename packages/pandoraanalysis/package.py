# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Pandoraanalysis(CMakePackage, Ilcsoftpackage):
    """Pandora calibration and analysis tools in iLCSoft / Marlin framework"""

    url = "https://github.com/PandoraPFA/LCPandoraAnalysis/archive/v02-00-01.tar.gz"
    homepage = "https://github.com/PandoraPFA/LCPandoraAnalysis"
    git = "https://github.com/PandoraPFA/LCPandoraAnalysis.git"

    tags = ["hep"]

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "2.0.1",
        sha256="cab082096921d60390054bb0da6afc5eaee4df28411266d4404f9b3f50048e39",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("lcio")
    depends_on("root")
    depends_on("dd4hep")

    def setup_run_environment(self, spack):
        spack.prepend_path("MARLIN_DLL", self.prefix.lib + "/libPandoraAnalysis.so")

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
