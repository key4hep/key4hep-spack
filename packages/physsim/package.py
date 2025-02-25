# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Physsim(CMakePackage, Ilcsoftpackage):
    """Physsim is a matrix element package."""

    url = "https://github.com/iLCSoft/Physsim/archive/v00-04-01.tar.gz"
    homepage = "https://github.com/iLCSoft/Physsim"
    git = "https://github.com/iLCSoft/Physsim.git"

    maintainers = ["vvolkl"]

    tags = ["hep"]

    version("master", branch="master")
    version(
        "0.5",
        sha256="f1313ceb5e13084e1f31a697086deaf626570d3e660aee58691e17f7000c7fe6",
    )
    version(
        "0.4.2",
        sha256="fc3aa07b498e24c878c13937207d59baefd73ce36707203d3856ee0aae6459e4",
    )
    version(
        "0.4.1",
        sha256="4c22eee5dcccb764a5ff90850aeb33563c45a14af8939a3ebea736c7d92ac1c1",
    )

    depends_on("ilcutil")
    depends_on("root")

    patch("dict.patch")
    patch("TString_include.patch", when="@:0.4.1")

    def setup_run_environment(self, env):
        # The dictionary headers require physsim to be in CPATH or ROOT_INCLUDE_PATH
        env.prepend_path("CPATH", self.prefix.include.physsim)

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args
