# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cldconfig(CMakePackage):
    """Configuration files for the CLD detector concept"""

    homepage = "https://github.com/key4hep/CLDConfig"
    git = "https://github.com/key4hep/CLDConfig"

    maintainers = ["jmcarcell"]

    version("main", branch="main")
    # Old tag to make sure there is at least one, can be removed when
    # there is another
    version("r2024-04-12", tag="r2024-04-12")

    depends_on("k4geo", type="test")
    depends_on("dd4hep", type="test")
    depends_on("k4fwcore", type="test")
    depends_on("k4marlinwrapper", type="test")
    depends_on("marlintrkprocessors", type="test")
    depends_on("conformaltracking", type="test")
    depends_on("ddmarlinpandora", type="test")
    depends_on("clicperformance", type="test")
    depends_on("lcfiplus", type="test")
    depends_on("marlinfastjet", type="test")

    def cmake_args(self):
        args = []
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.set("CLDCONFIG", self.prefix)
