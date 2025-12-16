# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lcfiplus(CMakePackage, Ilcsoftpackage):
    """Flavor tagging code for ILC detectors, for documentation consult confluence at https://confluence.slac.stanford.edu/display/ilc/LCFIPlus"""

    url = "https://github.com/lcfiplus/LCFIPlus/archive/v00-10.tar.gz"
    homepage = "https://github.com/lcfiplus/LCFIPlus"
    git = "https://github.com/lcfiplus/LCFIPlus.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "0.11.1",
        sha256="3e15a6d14c1569c237884f5d5ee57860733e37682401baf0e55e7f406f90c78b",
    )
    version(
        "0.11",
        sha256="db034e7738d107ea128efaef65071856218324a841db9cd6186b01a6acd054ae",
    )
    version(
        "0.10.1",
        sha256="4eac91718b29de926f7cd5bc7aa879d157bfec8f4306ccd1d74785813569fde0",
    )
    version(
        "0.10",
        sha256="0d4d27cd0d9407cd2f13e5a978be8c9389bc86c78c2eefd0ae7c060c4b7196c3",
    )

    patch("dict.patch", when="@0.10:0.10.1")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("lcfivertex")
    depends_on("root +tmva")

    def cmake_args(self):
        args = []
        args.append(self.define("INSTALL_DOC", False))
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    @run_after("install")
    def install_source(self):
        install_tree("include", self.prefix.include)

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libLCFIPlus.so")
