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
        "0.7", sha256="aff49b9885d3c5e0804d5bcd3752ac77f3e3bbce6910fa9277252b907656914a"
    )

    depends_on("root")
    depends_on("lcio")
    depends_on("marlin")
    depends_on("gaudi@35.0:")
    depends_on("k4fwcore")
    depends_on("edm4hep")
    depends_on("edm4hep@0.10:1")
    depends_on("k4edm4hep2lcioconv")
    # for the doctest:
    depends_on("py-jupytext", type=("test"))
    depends_on("py-ipykernel", type=("test"))
    depends_on("py-nbconvert", type=("test"))

    def cmake_args(self):
        args = [self.define("FORCE_COLORED_OUTPUT", False)]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PATH", self.prefix.scripts)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4marlinwrapper"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4marlinwrapper"].prefix.lib64)
        env.set("K4MARLINWRAPPER", self.prefix.share.k4MarlinWrapper)

    def setup_build_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4fwcore"].prefix.lib64)
