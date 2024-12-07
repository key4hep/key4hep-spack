# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinreco(CMakePackage, Ilcsoftpackage):
    """Assembly of various Marlin processor for reconstruction."""

    url = "https://github.com/iLCSoft/MarlinReco/archive/v01-27.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinReco"
    git = "https://github.com/iLCSoft/MarlinReco.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.36.1",
        sha256="fc97edf00ea943f76340e20ccc57a8538292ed64e7b33b6f64e9ebc7a3da9320",
    )
    version(
        "1.36",
        sha256="3f0c9839567a58b629b4cba40088b095a6660cbd104d157edf6dd21f81471694",
    )
    version(
        "1.35",
        sha256="009ea04769776424b203f08c9af75f544b8cd93f379537285e24e3470bb52be8",
    )
    version(
        "1.34",
        sha256="d80a35307a1f4b0f94ae3c055b948b69d7686e33a194cd786e706631a11261f8",
    )
    version(
        "1.33.1",
        sha256="2c89954a3a83909e5da069ce223c3d5bd25bd911b7415a219456fbbed13953b8",
    )
    version(
        "1.33",
        sha256="4f5a9c091c26d67b6be6b1cf2fc1fd57445302a4f817a4aea021c51a3fdc7424",
    )
    version(
        "1.32",
        sha256="0ea3bee03e2bec1924b5876675043b592a942bc8cf306eb7056eaf03ac1748f6",
    )

    patch("algorithm.patch", when="@:1.36")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("marlinutil@1.17.1:", when="@1.34:")
    depends_on("marlinkinfit")
    depends_on("marlintrk")
    depends_on("gsl")
    depends_on("root")
    depends_on("boost")
    depends_on("dd4hep")
    depends_on("raida")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libMarlinReco.so")

    def cmake_args(self):
        # C++ Standard
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
