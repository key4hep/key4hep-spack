# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Ddmarlinpandora(CMakePackage, Key4hepPackage):
    """Interface between Gaudi and PandoraPFA."""

    url = "https://github.com/key4hep/k4GaudiPandora/archive/v00-11.tar.gz"
    homepage = "https://github.com/key4hep/k4GaudiPandora.git"
    git = "https://github.com/key4hep/k4GaudiPandora.git"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("lccontent")
    depends_on("pandorapfa")
    depends_on("pandorasdk")
    depends_on("root")

    def setup_run_environment(self, env):
        env.prepend_path(
            "LD_LIBRARY_PATH", self.spec["k4gaudipandora"].libs.directories[0]
        )

    def cmake_args(self):
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
