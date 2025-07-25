# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Kitrack(CMakePackage, Ilcsoftpackage):
    """Toolkit for Tracking. Consists of KiTrack (Cellular Automaton, a Hopfield Neural Network, the hit and track classes) and Criteria (the criteria classes)."""

    url = "https://github.com/iLCSoft/KiTrack/archive/v01-10.tar.gz"
    homepage = "https://github.com/iLCSoft/KiTrack"
    git = "https://github.com/iLCSoft/KiTrack.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.10.1",
        sha256="ccfd9317168814350d089a406cc7ed0cf1b44e9aa71e846faf8f0ab4113c7adf",
    )
    version(
        "1.10",
        sha256="e89e0553ba76946749e422aa470bbe20456b085efe523fb42f97565201376870",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args
