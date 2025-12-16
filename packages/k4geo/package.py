# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class K4geo(CMakePackage):
    """DD4hep geometry models for future colliders."""

    homepage = "https://github.com/key4hep/k4geo"
    git = "https://github.com/key4hep/k4geo.git"
    url = "https://github.com/key4hep/k4geo/archive/v00-16-07.tar.gz"

    generator = "Ninja"

    maintainers("jmcarcell")

    version("main", branch="main")
    version(
        "00-24",
        sha256="3eefd973c0e534cc5cbb4d8fc079455508986bba49f859c30e0c23ac3e732f19",
    )
    version(
        "00-23",
        sha256="dd0c6300a6a2190a089012dfea271bd31050e8d4134ce09d896ebd81ef7391c5",
    )
    version(
        "00-22",
        sha256="95712eaf3452d29d35ac8156c37e5b4ea6449eb04073fb330bddc5df686f2cb3",
    )
    version(
        "0.21",
        sha256="0451e532fd22b2b9ea93a71f7036ea6de44386ecb10a84f28bc1d9fd557c6ad1",
        url="https://github.com/key4hep/k4geo/archive/refs/tags/v00-21.tar.gz",
    )
    version(
        "0.20.0",
        sha256="40d5842faa4767cc1b8c19f9b710713ba6a128ecd94fb9682e3afe3145e20511",
    )
    version(
        "0.19.0",
        sha256="6e8101e5991870484988f9fcb0299076a30f9b5f37e4e51141e50dfd30f32314",
    )

    version(
        "0.18.1",
        sha256="2bcdcbb772b9672994ac3cf8e9691f55f23a898d67c6f6c84ae0ae1b5416d893",
    )
    version(
        "0.18",
        sha256="50cd058e80baba21748156f3603a45a2388c6f3a8823d9aaa3f419eb58038fc9",
    )

    variant("compact", default=True, description="Install compact files")

    depends_on("cxx", type="build")

    depends_on("lcio")
    depends_on("dd4hep")
    depends_on("dd4hep@1.31:", when="@0.22:")
    depends_on("root")
    depends_on("python", type="build")
    depends_on("ninja", type="build")
    depends_on("podio")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        args.append(self.define_from_variant("INSTALL_COMPACT_FILES", "compact"))
        # Automatically install the CAD beampipe files if we install the compact files
        args.append(
            self.define(
                "INSTALL_BEAMPIPE_STL_FILES", self.spec.variants["compact"].value
            )
        )
        args.append(self.define("BUILD_TESTING", self.run_tests))
        return args

    def setup_run_environment(self, env):
        env.set("LCGEO", self.prefix.share.k4geo)
        env.set("K4GEO", self.prefix.share.k4geo)
        env.set("lcgeo_DIR", self.prefix.share.k4geo)
        env.set("k4geo_DIR", self.prefix.share.k4geo)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].libs.directories[0])

    def setup_build_environment(self, env):
        env.set("LCGEO", self.prefix.share.k4geo)
        env.set("lcgeo_DIR", self.prefix.share.k4geo)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["lcio"].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.set("LCGEO", self.prefix.share.k4geo)
        env.set("lcgeo_DIR", self.prefix.share.k4geo)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.spec["lcio"].libs.directories[0])

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("LCGEO", self.prefix.share.k4geo)
        env.set("lcgeo_DIR", self.prefix.share.k4geo)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.spec["lcio"].libs.directories[0])

    # dd4hep tests need to run after install step:
    # disable the usual check
    def check(self):
        pass

    # instead add custom check step that runs after installation
    @run_after("install")
    def install_check(self):
        print(self)
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
