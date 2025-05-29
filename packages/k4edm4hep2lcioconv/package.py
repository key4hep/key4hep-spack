# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4edm4hep2lcioconv(CMakePackage, Key4hepPackage):
    """Converter library between EDM4hep and LCIO"""

    homepage = "https://github.com/key4hep/k4EDM4hep2LcioConv"
    git = "https://github.com/key4hep/k4EDM4hep2LcioConv.git"
    url = (
        "https://github.com/key4hep/k4EDM4hep2LcioConv/archive/refs/tags/v00-10.tar.gz"
    )

    maintainers("tmadlener")

    version("main", branch="main")
    version(
        "00-12",
        sha256="4a435456d029657d6bb4f6406e7060bb9934a96370b356a8972268e95f80bcf1",
    )
    version(
        "00-11",
        sha256="937c9a794f094395134ed4df448fda643e0ba4a339b7ee1d8d2e4ea08f4ee2f7",
    )
    version(
        "00-10",
        sha256="a7fbdb0dfc3082b71f158a1c0a7f3c7698901b1f2bc9204cf7e9c656ae142884",
        deprecated=True,
    )
    version(
        "00-09",
        sha256="aae9ac39ae56f9e18b8b2f13c84ca95a2c90b71069a5318b894a574d773d8815",
    )

    depends_on("lcio@2.20:")
    depends_on("lcio@2.20.1:", when="@00-08:")
    depends_on("lcio@2.22:", when="@00-09:")
    depends_on("podio")
    depends_on("podio@1:", when="@00-09:")
    depends_on("edm4hep@0.10:")
    depends_on("edm4hep@0.99:", when="@00-09:")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
        ]
        return args

    def setup_run_environment(self, env):
        env.set("K4EDM4HEP2LCIOCONV", self.prefix.share.k4EDM4hep2LcioConv)
