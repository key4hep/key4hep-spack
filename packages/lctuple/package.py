# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lctuple(CMakePackage, Ilcsoftpackage):
    """Marlin package that creates a ROOT TTree with a column wise ntuple from LCIO collections."""

    url = "https://github.com/iLCSoft/LCTuple/archive/v01-12.tar.gz"
    homepage = "https://github.com/iLCSoft/LCTuple"
    git = "https://github.com/iLCSoft/LCTuple.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.14",
        sha256="7088a6923c4e4c3ac327965c8d41f53eb1403134a9df52e43635fa5eaef48581",
    )
    version(
        "1.13",
        sha256="35f2ff3d4b89a3fd7e87f6f5c9fec2178afec26ae8c89d30a5b0bcf113d2107f",
    )
    version(
        "1.12",
        sha256="e0e7c4c86f257027a7e9b1c42438087a7b0919964f9719080be25df8a0f95968",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("root")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libLCTuple.so")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args
