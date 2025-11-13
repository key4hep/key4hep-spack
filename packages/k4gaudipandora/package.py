# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4gaudipandora(CMakePackage, Key4hepPackage):
    """Interface between Gaudi and PandoraPFA."""

    url = "https://github.com/key4hep/k4GaudiPandora/archive/v00-11.tar.gz"
    homepage = "https://github.com/key4hep/k4GaudiPandora.git"
    git = "https://github.com/key4hep/k4GaudiPandora.git"

    maintainers("jmcarcell")

    version("main", branch="main")
    version(
        "0.1.0",
        sha256="a77e7f76728c14054f112e923b55e434becafb7d392e2f3653133a5e8ad2d235",
    )

    depends_on("cxx", type="build")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("lccontent")
    depends_on("pandorasdk")
    depends_on("root")
    depends_on("k4reco")

    # Used in the tests
    depends_on("k4geo")

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4gaudipandora"].prefix.lib)

    def cmake_args(self):
        return [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            "-DCMAKE_INSTALL_LIBDIR=lib",
        ]
