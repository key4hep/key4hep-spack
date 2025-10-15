# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ddmarlinpandora(CMakePackage, Ilcsoftpackage):
    """Interface between Marlin and PandoraPFA."""

    url = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"
    homepage = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"
    git = "https://github.com/iLCSoft/DDMarlinPandora.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "0.14",
        sha256="9c8de305d65007e2ce22489f961e469111d24b1c850dac5efc237019bd4da28e",
    )
    version(
        "0.13",
        sha256="80274bba9bc4ce53f0d78132bd5aba82f03000a527c2eed3adc5c33f12d194f3",
    )
    version(
        "0.12.2",
        sha256="c9d9461aee2eb2db81f4369583a84f6f0d5261db5d06f641bcd16704b62096fe",
    )
    version(
        "0.12.01",
        sha256="c1c44db7a375022ad18e0a44f0c8e573c7cd9db1a7c1b6b4ac58998e20007048",
    )
    version(
        "0.12",
        sha256="4f90c2ef240c2fa1f293498bf35201d1337651f8847d53da7124a61091bb504e",
    )
    version(
        "0.11",
        sha256="92410186209508091e0a8e330986283ffb32e40fd7195d10aad1a6a2e953f3ee",
    )

    depends_on("c", type="build", when="@:0.13")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("marlinutil")
    depends_on("marlin")
    depends_on("pandorasdk")
    depends_on("pandorapfa")
    depends_on("lccontent")
    depends_on("larcontent")
    depends_on("dd4hep")
    depends_on("marlintrk")
    depends_on("pandoramonitoring", when="+monitoring")

    variant("monitoring", default=False, description="Enable Pandora Monitoring")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libDDMarlinPandora.so")

    def cmake_args(self):
        return [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define_from_variant("PANDORA_MONITORING", "monitoring"),
        ]
