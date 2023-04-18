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

    maintainers("tmadlener")

    version("master", branch="master")
    version(
        "00-03",
        sha256="0b7fffbe1a07aae4b5b7523e855e944fe90f6e072dae9a460a07134025bf1cf8",
    )
    version(
        "00-02-01",
        sha256="747066a7f060c4ce6136c1636f90f5f8a20cfb0c474258cbf92cd1a1c28ee394",
    )
    version(
        "00-02",
        sha256="b9478ed8811bb99103df387db1e2a2cc97bb8d31a6d7b9bf17e6ba6f8ebef153",
    )
    version(
        "00-01",
        sha256="a1eb60337033658888c637af7c4c57622513a708834fb8a67e6b984614b45748",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/key4hep/k4EDM4hep2LcioConv/pull/2.patch",
        when="@00-01",
        sha256="09dda24dc561b8b3eb7336c69fec7535ba2e1cd44b4470e3fe655e3c00a79d86",
    )

    depends_on("lcio")
    depends_on("podio")
    depends_on("edm4hep@0.4.1:")
    depends_on("edm4hep@0.5:", when="@00-02-01:")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("FORCE_COLORED_OUTPUT", False),
        ]
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("K4EDM4HEP2LCIOCONV", self.prefix.share.k4EDM4hep2LcioConv)
