# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class K4generatorsconfig(CMakePackage):
    """A python based module for the automatic generation of inputfiles for Monte-Carlo(MC) generators."""

    homepage = "https://github.com/key4hep/k4GeneratorsConfig"
    git = "https://github.com/key4hep/k4GeneratorsConfig.git"
    # To be changed once there is a first version
    url = "https://github.com/key4hep/k4GeneratorsConfig.git/archive/v00-16-07.tar.gz"

    generator = "Ninja"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    depends_on("podio")
    depends_on("edm4hep")
    depends_on("hepmc3")
    depends_on("heppdt")
    depends_on("pythia8")
    depends_on("python@3.7:")
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
