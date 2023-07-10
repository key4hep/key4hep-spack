# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class K4geo(CMakePackage):
    """DD4hep geometry models for future colliders."""

    homepage = "https://github.com/key4hep/k4geo"
    git = "https://github.com/key4hep/k4geo.git"
    url = "https://github.com/key4hep/k4geo/archive/v00-16-07.tar.gz"

    generator = "Ninja"

    maintainers = ["jmcarcell"]

    version("master", branch="master")
    version(
        "0.18.1",
        sha256="2bcdcbb772b9672994ac3cf8e9691f55f23a898d67c6f6c84ae0ae1b5416d893",
    )
    version(
        "0.18",
        sha256="50cd058e80baba21748156f3603a45a2388c6f3a8823d9aaa3f419eb58038fc9",
    )
    version(
        "0.17",
        sha256="4b515895df7a65b0c1f4061a8947b1bbb4c727b924ad73a1f03722de31327c3f",
    )
    version(
        "0.16.8",
        sha256="6ce3ec018aa2b86a50f7c2dd868c0bd9d46b413bdde70139fcbe2f8167bb835a",
    )
    version("0.16.7", tag="v00-16-07")
    version(
        "0.16.6",
        sha256="76593d4f339c5e89acdb878de1f48eb46d9a9faf9c7e1bcac8346c235c2508c6",
    )
    version(
        "0.16.5",
        sha256="e6d88dcca5440632241c30cab7bc0d314afef42a7a7ff15b68fc59cf997cda08",
    )

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("lcio")
    depends_on("dd4hep")
    depends_on("lcio")
    depends_on("boost")
    depends_on("root")
    depends_on("python", type="build")
    depends_on("ninja", type="build")

    patch(
        "https://patch-diff.githubusercontent.com/raw/key4hep/k4geo/pull/255.diff",
        sha256="fc39117d3b579ab383077fd7274d321f1e954cefa9e481b45310cd36b35aa3dd",
        when="@0.16.8",
    )
    patch(
        "https://github.com/key4hep/k4geo/commit/cb87609446255c3a94da867ad7801a62ff3b6b05.patch",
        sha256="3e02ca5c89558342d8fd2489463c285af5a5500baeba2faf8d41f8ec3ae2f487",
        when="@0.16.7",
    )

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        args.append(self.define("BUILD_TESTING", self.run_tests))
        return args

    @run_after("install")
    def install_compact(self):
        install_tree("CaloTB", self.prefix.share.k4geo.compact.CaloTB)
        install_tree("CLIC", self.prefix.share.k4geo.compact.CLIC)
        install_tree("FCalTB", self.prefix.share.k4geo.compact.FCalTB)
        install_tree("FCCee", self.prefix.share.k4geo.compact.FCCee)
        install_tree("fieldmaps", self.prefix.share.k4geo.compact.fieldmaps)
        install_tree("ILD", self.prefix.share.k4geo.compact.ILD)
        install_tree("SiD", self.prefix.share.k4geo.compact.Sid)

    def setup_run_environment(self, env):
        env.set("LCGEO", self.prefix.share.k4geo.compact)
        env.set("K4GEO", self.prefix.share.k4geo.compact)
        env.set("lcgeo_DIR", self.prefix.share.k4geo.compact)
        env.set("k4geo_DIR", self.prefix.share.k4geo.compact)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].prefix.lib64)

    def setup_build_environment(self, env):
        env.set("LCGEO", self.prefix.share.k4geo.compact)
        env.set("lcgeo_DIR", self.prefix.share.k4geo.compact)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["lcio"].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("LCGEO", self.prefix.share.k4geo.compact)
        env.set("lcgeo_DIR", self.prefix.share.k4geo.compact)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4geo"].prefix.lib64)
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
