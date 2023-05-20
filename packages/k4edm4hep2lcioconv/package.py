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

    version("master", branch="master")
    version(
        "00-04",
        sha256="1b6db84f42a1d6e2e5a02cecbc01a0282081b7270a523f201fad4d39f78ca015",
    )
    version(
        "00-03",
        sha256="0b7fffbe1a07aae4b5b7523e855e944fe90f6e072dae9a460a07134025bf1cf8",
    )

    depends_on("lcio")
    depends_on("podio")
    depends_on("edm4hep@0.5:", when="@00-03")
    depends_on("edm4hep@0.8:", when="@00-04:")

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
