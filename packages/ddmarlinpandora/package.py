# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ddmarlinpandora(CMakePackage, Ilcsoftpackage):
    """Interface between Marlin and PandoraPFA."""

    url = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"
    homepage = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"
    git = "https://github.com/iLCSoft/DDMarlinPandora.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "0.12",
        sha256="4f90c2ef240c2fa1f293498bf35201d1337651f8847d53da7124a61091bb504e",
    )
    version(
        "0.11",
        sha256="92410186209508091e0a8e330986283ffb32e40fd7195d10aad1a6a2e953f3ee",
    )

    depends_on("ilcutil")
    depends_on("marlinutil")
    depends_on("marlin")
    depends_on("pandorasdk")
    depends_on("pandorapfa")
    depends_on("lccontent")
    depends_on("larcontent")
    depends_on("dd4hep")
    depends_on("marlintrk")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libDDMarlinPandora.so")

    def cmake_args(self):
        # C++ Standard
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
