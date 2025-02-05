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
    url = "https://github.com/key4hep/k4EDM4hep2LcioConv/archive/v00-01.zip"

    maintainers = ["tmadlener"]

    version("main", branch="main")
    version(
        "00-10",
        sha256="d0d082d9dee973819d7713d883507a0303dbd917fb14c3749a4ffcdafc4e4af2",
    )
    version(
        "00-09",
        sha256="bdbb88e2900eb3834d74d100b4d32ae760ee0816ac5fa4a5930772fbe9fb11d9",
    )
    version(
        "00-08-02",
        sha256="a0418b5c3c6ce77435bd942279420b0390099f417a7984227cf212710b079321",
        deprecated=True,
    )
    version(
        "00-08-01",
        sha256="4518e39a0c87182d394f213074344ed29724005cd0481a2555a1fe48fdb98d2b",
        deprecated=True,
    )
    version(
        "00-08",
        sha256="e3bfcb611b78d8e457d7f68e25d5aabe21b4b87928b0de0fc61a09734c7adb4c",
        deprecated=True,
    )
    version(
        "00-07",
        sha256="269d14c390f987fb3fdb0d2e952febfb639415bef50e5e1c8992f23e0cd4a5a6",
        deprecated=True,
    )
    version(
        "00-06",
        sha256="c220604577d309bc11a5a4c147f55640fedef90375d1232439343362607a3906",
        deprecated=True,
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
