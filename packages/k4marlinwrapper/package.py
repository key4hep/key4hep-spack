# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class K4marlinwrapper(CMakePackage, Ilcsoftpackage):
    """Gaudify Marlin Processors in order to run them in the Key4HEP framework"""

    homepage = "https://github.com/key4hep/k4MarlinWrapper"
    git = "https://github.com/key4hep/k4MarlinWrapper.git"
    url = "https://github.com/key4hep/k4MarlinWrapper/archive/v00-01.tar.gz"

    maintainers = ["tmadlener", "jmcarcell"]

    version("master", branch="master")
    version(
        "0.6", sha256="8f276fe5246c12e3ccf460a03a5621a129f172a5047cf7321957f1eeb807f821"
    )
    version(
        "0.5", sha256="080f86700fd141b288878688a5c8f14fe48f1247a4fa1ce37147f528484e826a"
    )
    version(
        "0.4.2",
        sha256="8ec51ba4e0348d67377179e9d3e9043267a42a0d360d884c331ce52c51b61b03",
    )
    version(
        "0.4.1",
        sha256="7e3c76bd21a2f2bea196fcae270e29e26ed2abc8d70a4c3d37ce88bacbd22528",
    )
    version(
        "0.4", sha256="6609dacb158f8fd2f8532e0881b0acb73ea23f31578eab44085876a8a59a5946"
    )
    version(
        "0.3.1",
        sha256="a8ef66f6500b9a709b950cdfd3bcb0c775d7fa42336b2aa5c80e2efef7c95b19",
    )
    version(
        "0.3", sha256="381fd96e2ede03bec048afaeef13b8efffe80030fc097fe18fae62b03c0fba94"
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/key4hep/k4MarlinWrapper/pull/81.diff",
        sha256="86348f9e346decb70e88fc0aa071630b97b155660314a01eed3e44e447d00d10",
        when="@0.4.1",
    )

    depends_on("root")
    depends_on("lcio")
    depends_on("marlin")
    depends_on("gaudi@35.0:")
    depends_on("k4fwcore")
    depends_on("edm4hep")
    depends_on("edm4hep@0.4.1:", when="@0.4.1:")
    depends_on("edm4hep@0.8:", when="@0.6:")
    depends_on("k4lcioreader")
    depends_on("k4edm4hep2lcioconv", when="@0.4.2:")
    depends_on("wget", type=("test"))
    depends_on("catch2@3.0.1:", when="@0.3.2:", type=("test"))
    # for the doctest:
    depends_on("py-jupytext", type=("test"))
    depends_on("py-ipykernel", type=("test"))
    depends_on("py-nbconvert", type=("test"))

    def cmake_args(self):
        args = [self.define("FORCE_COLORED_OUTPUT", False)]
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib64)
        spack_env.set("K4MARLINWRAPPER", self.prefix.share.k4MarlinWrapper)

    def setup_build_environment(self, spack_env):
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib)
