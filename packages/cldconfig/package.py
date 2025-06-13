# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cldconfig(CMakePackage):
    """Configuration files for the CLD detector concept"""

    homepage = "https://github.com/key4hep/CLDConfig"
    git = "https://github.com/key4hep/CLDConfig"
    url = "https://github.com/key4hep/CLDConfig/archive/refs/tags/r2024-10-06.tar.gz"

    maintainers("jmcarcell")

    version("main", branch="main")
    version(
        "2025-05-26",
        sha256="9be425b074331c8b5ffeefd57af3d3c8242fa7639665cfb9b7a99d6cc09320e8",
    )
    version(
        "2024-10-06",
        sha256="7ded5bc3f63eed6b6806d9581e1b47d7ca14a0c97ef5d61331d4ef88b1d7d643",
    )
    version(
        "2024-04-12",
        sha256="8a15971152391da3b41bbf543316ad6b41949cd3d3c82e334a7a7b86092591da",
    )

    depends_on("cxx", type="build")

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
