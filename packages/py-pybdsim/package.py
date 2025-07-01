# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPybdsim(PythonPackage):
    """Utilities for preparing and analysing BDSIM input and output as well as controlling BDSIM"""

    homepage = "https://github.com/bdsim-collaboration/pybdsim"
    url = "https://github.com/bdsim-collaboration/pybdsim/archive/v3.6.1.tar.gz"
    git = "https://github.com/bdsim-collaboration/pybdsim.git"

    tags = ["hep"]

    maintainers("jmcarcell")

    version("master", branch="master")

    version(
        "3.6.1",
        sha256="9308648b2745d60fe5da6c9422bbe8ea2f177f1987cd949ece01ab88b55bb339",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-importlib-resources", type=("build", "run"))

    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-scipy")
    depends_on("py-fortranformat")
    depends_on("py-jinja2")

    depends_on("py-pymadx")
    depends_on("py-pytransport")

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.spec["py-importlib-resources"].prefix.lib)
