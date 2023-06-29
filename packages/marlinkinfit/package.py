# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinkinfit(CMakePackage, Ilcsoftpackage):
    """Kinematic Fitting Library for Marlin"""

    url = "https://github.com/iLCSoft/MarlinKinfit/archive/v00-06.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinKinfit"
    git = "https://github.com/iLCSoft/MarlinKinfit.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "0.6.1",
        sha256="06732df9e8f5f17841ae6de2f7a6cf1b6e80de1064e9cb013906cdd015c00f61",
    )
    version(
        "0.6", sha256="e22127f3d349c5b5a6a1c95585f5bf410d77cf598b3432b188f781436632372a"
    )

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("clhep")
    depends_on("gsl")
    depends_on("root")
    depends_on("raida")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libMarlinKinfit.so")
