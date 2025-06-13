# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Forwardtracking(CMakePackage, Ilcsoftpackage):
    """Track Reconstruction for the Forward Direction (for the FTD)"""

    url = "https://github.com/iLCSoft/ForwardTracking/archive/v01-14.tar.gz"
    homepage = "https://github.com/iLCSoft/ForwardTracking"
    git = "https://github.com/iLCSoft/ForwardTracking.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.14.2",
        sha256="daa9ea4d837cba4ef337c63b439b3c25c7ae324bfc7b6bda2634e61dfc42c35f",
    )
    version(
        "1.14.1",
        sha256="39f2a858baaedd703dbc30f0c813c641d63dcac8e735716730bb3d46ca3e474f",
    )
    version(
        "1.14",
        sha256="99149d170a1ae179500b2c47ec79dca227ff96c0bdf0cd69f2075eb468177a5e",
    )

    patch("testing.patch", when="@:1.15")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("marlintrk")
    depends_on("kitrack")
    depends_on("kitrackmarlin")
    depends_on("gsl")
    depends_on("root")
    depends_on("clhep")
    depends_on("raida")

    def cmake_args(self):
        args = []
        args.append(self.define("BUILD_TESTING", self.run_tests))
        args.append(
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            )
        )
        return args

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libForwardTracking.so")
