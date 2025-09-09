# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cluestering(CMakePackage):
    """High-performance density-based clustering library developed at CERN""" 

    url = "https://github.com/cms-patatrack/CLUEstering/archive/refs/tags/2.7.0.tar.gz"
    git = "https://github.com/cms-patatrack/CLUEstering.git"
    homepage = "https://github.com/cms-patatrack/CLUEstering"

    maintainers("jmcarcell")

    tags = ["hep"]

    version("main", branch="main")

    version(
        "2.7.0",
        sha256="bb2c7b8e3301f87261b1da874dce62bdd9630b6ff020846f6b8b3e774a2697b9",
    )

    depends_on("boost")
    depends_on("alpaka")

    def cmake_args(self):
        args = [
            self.define("BUILD_PYTHON", False),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        return args
