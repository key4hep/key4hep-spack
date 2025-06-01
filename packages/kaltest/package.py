# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Kaltest(CMakePackage, Ilcsoftpackage):
    """Kaltest tracking software."""

    homepage = "https://github.com/iLCSoft/KalTest"
    url = "https://github.com/iLCSoft/KalTest/archive/v02-05.tar.gz"
    git = "https://github.com/iLCSoft/KalTest.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "2.5.2",
        sha256="6f17d25fdfa6fc01c733a5ef5cb7e89e110165d77c9891f606928d496bda7d6a",
    )
    version(
        "2.5.1",
        sha256="2e3470b8f7f87aab02c823c8e7435294e31adb9b018460016054fbace3915f4d",
    )
    version(
        "2.5", sha256="8753ecf5ed7819744cc66a652cf8ddcd0d783a25ee19b5387212f70dd9abbce5"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("root")

    patch("dict.patch")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        # The dictionary headers required kaltest to be in CPATH or ROOT_INCLUDE_PATH
        # other libraries require include to be searchable (which is automatic)
        env.prepend_path("CPATH", self.prefix.include.kaltest)
