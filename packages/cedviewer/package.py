# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Cedviewer(CMakePackage, Ilcsoftpackage):
    """CEDViewer: Marlin processor for the CED event display."""

    url = "https://github.com/iLCSoft/CEDViewer/archive/v01-17-01.tar.gz"
    homepage = "https://github.com/iLCSoft/CEDViewer"
    git = "https://github.com/iLCSoft/CEDViewer.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.20",
        sha256="e2b1b50b42be28aa28bbdba99e403e053a1aff7bcd7c76c6b7224768a3d28c68",
    )
    version(
        "1.19.1",
        sha256="aaa5317ae35d11a2850d623667607fc130181ea500a596e3073f744deae0f8b6",
    )
    version(
        "1.19",
        sha256="3446ce55b93de37a84b022c0a3a33097f2089c75dd91b4b5c84c6183ddeb5a01",
    )
    version(
        "1.18",
        sha256="46d188d102cbb414b4534e357e506c370644f2df8eada5565a2bcf234a282141",
    )
    version(
        "1.17.1",
        sha256="e778396dc6d9c106888c30bc11695a2283be68a5ced155df72cd5ec7d3c3f648",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ced")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("ilcutil")
    depends_on("dd4hep")
    depends_on("root")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libCEDViewer.so")

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
