# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPybdsim(PythonPackage):
    """Utilities for preparing and analysing BDSIM input and output as well as controlling BDSIM"""

    homepage = "https://bitbucket.org/jairhul/pybdsim"
    url = "https://bitbucket.org/jairhul/pybdsim/get/v3.6.1.tar.gz"
    git = "https://bitbucket.org/jairhul/pybdsim.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version("master", branch="master")

    version(
        "3.6.1",
        sha256="7bb7ba5d0f911dfc0115dce5b4a946743b34971836ef4112b2ede2195826cc11",
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
