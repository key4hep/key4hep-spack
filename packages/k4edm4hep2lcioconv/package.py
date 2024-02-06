# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4edm4hep2lcioconv(CMakePackage, Key4hepPackage):
    """Converter library between EDM4hep and LCIO"""

    homepage = "https://github.com/key4hep/k4EDM4hep2LcioConv"
    git = "https://github.com/key4hep/k4EDM4hep2LcioConv.git"
    url = "https://github.com/key4hep/k4EDM4hep2LcioConv/archive/v00-01.zip"

    maintainers = ["tmadlener"]

    version("main", branch="main")
    version(
        "00-08-01",
        sha256="4518e39a0c87182d394f213074344ed29724005cd0481a2555a1fe48fdb98d2b",
    )
    version(
        "00-08",
        sha256="e3bfcb611b78d8e457d7f68e25d5aabe21b4b87928b0de0fc61a09734c7adb4c",
    )
    version(
        "00-07",
        sha256="269d14c390f987fb3fdb0d2e952febfb639415bef50e5e1c8992f23e0cd4a5a6",
    )
    version(
        "00-06",
        sha256="c220604577d309bc11a5a4c147f55640fedef90375d1232439343362607a3906",
    )
    version(
        "00-05",
        sha256="6d352bacff6a16f8d2643cdb108794d02889c38b119442c3c260f9a75cb63e7a",
    )
    version(
        "00-04",
        sha256="1b6db84f42a1d6e2e5a02cecbc01a0282081b7270a523f201fad4d39f78ca015",
    )
    version(
        "00-03",
        sha256="0b7fffbe1a07aae4b5b7523e855e944fe90f6e072dae9a460a07134025bf1cf8",
    )

    depends_on("lcio")
    depends_on("lcio@2.20:", when="@00-05:")
    depends_on("lcio@2.20.1:", when="@00-08:")
    depends_on("podio")
    depends_on("edm4hep@0.5:", when="@00-03")
    depends_on("edm4hep@0.8:", when="@00-04:")
    depends_on("edm4hep@0.10:", when="@00-05:")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("FORCE_COLORED_OUTPUT", False),
        ]
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_run_environment(self, env):
        env.set("K4EDM4HEP2LCIOCONV", self.prefix.share.k4EDM4hep2LcioConv)
