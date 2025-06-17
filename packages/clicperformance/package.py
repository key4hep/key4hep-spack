# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Clicperformance(CMakePackage, Ilcsoftpackage):
    """Package containing processors and configurations to determine the performance of the CLIC detector model"""

    url = "https://github.com/iLCSoft/ClicPerformance/archive/v02-04.tar.gz"
    homepage = "https://github.com/iLCSoft/ClicPerformance"
    git = "https://github.com/iLCSoft/ClicPerformance.git"

    maintainers("vvolkl")

    generator = "Ninja"

    version("master", branch="master")
    version(
        "02-05-01",
        sha256="dd0b240cdab859b5ee60f0fac834207a2a426840553be39db2050eb51119977f",
    )
    version(
        "02-05",
        sha256="0205f79914a2422ee8db722ad53cbdc8722cb0867e7b57660ca9ec21fbb4e2ba",
    )
    version(
        "02-04-01",
        sha256="78fb40435eff722e81e29aaa7ad437cb17ee6f986d97242217a2fc66fbe1bf78",
    )
    version(
        "02-04-01",
        sha256="78fb40435eff722e81e29aaa7ad437cb17ee6f986d97242217a2fc66fbe1bf78",
    )
    version(
        "02-04",
        sha256="4e68230b558b3ba471b67d717bddabe609baa25f0228c18a2e8889ed9630f076",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("marlintrk")
    depends_on("gsl")
    depends_on("root")
    depends_on("dd4hep")
    depends_on("raida")
    depends_on("k4geo")

    depends_on("ninja", type="build")

    # for tests
    # TODO: investigate why type='test' does not work
    depends_on("marlindd4hep")
    depends_on("kaltest")
    depends_on("conformaltracking")
    depends_on("overlay")
    depends_on("marlinreco")
    depends_on("marlintrkprocessors")
    depends_on("ddmarlinpandora")
    depends_on("fcalclusterer")
    depends_on("lctuple")
    depends_on("marlinfastjet")
    depends_on("lcfiplus")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libClicPerformance.so")

    def setup_build_environment(self, env):
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["lcfiplus"].prefix.include)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["dd4hep"].prefix.lib)

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]

    # tests need installation, so skip here ...
    def check(self):
        pass

    # ... and  add custom check step that runs after installation instead
    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
