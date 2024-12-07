# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class K4generatorsconfig(CMakePackage):
    """A python based module for the automatic generation of inputfiles for Monte-Carlo(MC) generators."""

    homepage = "https://github.com/key4hep/k4GeneratorsConfig"
    git = "https://github.com/key4hep/k4GeneratorsConfig.git"
    url = "https://github.com/key4hep/k4GeneratorsConfig/archive/refs/tags/v0.1.tar.gz"

    generator = "Ninja"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    version(
        "0.1", sha256="0309f25bc4149de8c17a4615146074ece46f6f384a152e0fd05853ec652d9ad4"
    )

    depends_on("podio")
    depends_on("edm4hep")
    depends_on("hepmc3")
    depends_on("heppdt")
    depends_on("pythia8")
    depends_on("python")
    depends_on("py-pyyaml")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_run_environment(self, env):
        env.set("K4GENERATORSCONFIG", self.prefix.share.k4GeneratorsConfig)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.bin)
