# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class K4marlinwrapper(CMakePackage, Ilcsoftpackage):
    """Gaudify Marlin Processors in order to run them in the Key4hep framework"""

    homepage = "https://github.com/key4hep/k4MarlinWrapper"
    git = "https://github.com/key4hep/k4MarlinWrapper.git"
    url = "https://github.com/key4hep/k4MarlinWrapper/archive/v00-01.tar.gz"

    maintainers("tmadlener", "jmcarcell")

    version("main", branch="main")
    version(
        "00-12",
        sha256="f129269ec551a3fffe197763cdb742ca5690209c9f4213d59009fcb154adcdd4",
    )
    version(
        "0.11",
        sha256="e60a10c9ae1df3e07fb4823f12aba9dd0d8c32c7ee0e47583483fff8a6b0874e",
    )
    version(
        "0.10",
        sha256="7f04596f3825d0a8a9eb37aaeb546e03b245f8cb55fd5cdf2139e1ee2e8349ce",
    )
    version(
        "0.9", sha256="a0c01e6137cd5bb0794d79433831644dfd5108c763e436428117cd6f4a826ce2"
    )
    version(
        "0.8",
        sha256="0c624d5719cd055dfc27a9954cdf5e501e6478a2a8baac3bf80da7063e58e6ed",
        deprecated=True,
    )

    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("lcio")
    depends_on("marlin")
    depends_on("gaudi+gaudialg", when="@:0.8")
    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4fwcore@:1.1.0", when="@:0.9")
    depends_on("k4fwcore@1.2:", when="@0.11:")
    depends_on("edm4hep")
    depends_on("edm4hep@0.10.1:")
    depends_on("k4edm4hep2lcioconv")
    depends_on("k4edm4hep2lcioconv@:00-10", when="@:0.10")
    depends_on("k4edm4hep2lcioconv@00-11:", when="@0.11:")
    # for the doctest:
    depends_on("py-jupytext", type=("test"))
    depends_on("py-ipykernel", type=("test"))
    depends_on("py-nbconvert", type=("test"))
    # Uses GeoSvc from k4simgeant4
    depends_on("k4simgeant4", type=("test"))

    def cmake_args(self):
        args = [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4marlinwrapper"].prefix.lib)
        env.set("K4MARLINWRAPPER", self.prefix.share.k4MarlinWrapper)
