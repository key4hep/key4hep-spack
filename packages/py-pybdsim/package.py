# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPybdsim(PythonPackage):
    """Utilities for preparing and analysing BDSIM input and output as well as controlling BDSIM"""

    homepage = "https://bitbucket.org/jairhul/pybdsim"
    url = "https://bitbucket.org/jairhul/pybdsim"
    git = "https://bitbucket.org/jairhul/pybdsim.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version('master', branch='master')

    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-scipy")
    depends_on("py-fortranformat")
    depends_on("py-jinja2")

    depends_on("py-pymadx")
    depends_on("pytransport")
