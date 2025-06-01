# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Garlic(CMakePackage, Ilcsoftpackage):
    """Garlic is a Marlin Processor to identify photons and electrons."""

    url = "https://github.com/iLCSoft/Garlic/archive/v03-01.tar.gz"
    homepage = "https://github.com/iLCSoft/Garlic"
    git = "https://github.com/iLCSoft/Garlic.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "3.1", sha256="a35bea352d0c6aaa7d289656f6272be216e9b8ada2a750461ceed7c2cf780940"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("root")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libGarlic.so")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args
