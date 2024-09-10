# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class K4generatorsconfig(CMakePackage):
    """DD4hep geometry models for future colliders."""

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

    patch(
        "https://github.com/key4hep/k4GeneratorsConfig/commit/29f438dbc0955cf63c682c1bb2a27cd27273bc70.patch?full-index=1",
        sha256="4a970512113e4e474cd8a8f7db6c47f8decda500a7499088facc7adff17fc4e2"
    )

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_run_environment(self, env):
        env.set("K4GENERATORSCONFIG", self.prefix.share.k4geo)
