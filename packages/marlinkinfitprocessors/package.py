# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinkinfitprocessors(CMakePackage, Ilcsoftpackage):
    """A collection of Marlin processors that use the MarlinKinFit package"""

    url = "https://github.com/iLCSoft/MarlinKinfitProcessors/archive/v00-04-02.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinKinfitProcessors"
    git = "https://github.com/iLCSoft/MarlinKinfitProcessors.git"

    maintainers = ["vvolkl", "tmadlener"]

    version("master", branch="master")
    version(
        "0.5", sha256="0e560923e8af46b70b29973a6fda5ff459bb76e52452125b79a2397e9e0f5cfd"
    )
    version(
        "0.4.2",
        sha256="539d0e703c2b4f1416fa29c0bcef6e98c197d5c939c3b11c1474eb965da462fe",
    )
    version(
        "0.4.1",
        sha256="a6a1551239f909558d7cc31f9a06afb6a0c0124e0031d08bb2196097892bf19c",
    )
    version(
        "0.4", sha256="dbae3a81a6afa435bb6962544ba67797e137c224c17c3c0f43d3e0f3bb034db6"
    )

    variant("doc", default=False, description="build doxygen documentation")

    depends_on("marlinkinfit")
    depends_on("doxygen", when="+doc")

    def cmake_args(self):
        return [
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value,
            self.define_from_variant("INSTALL_DOC", "doc"),
        ]

    def setup_run_environment(self, env):
        env.prepend_path(
            "MARLIN_DLL", self.prefix.lib + "/libMarlinKinfitProcessors.so"
        )
