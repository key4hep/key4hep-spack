# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymadx(PythonPackage):
    """Utilities for processing and analysing MADX output"""

    homepage = "https://bitbucket.org/jairhul/pymadx"
    url = "https://bitbucket.org/jairhul/pymadx/get/v2.2.1.tar.gz"
    git = "https://bitbucket.org/jairhul/pymadx.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version("master", branch="master")

    version(
        "2.2.1",
        sha256="e329204931de9be8b0ab88e7ba92045136165c382f8de02f0e11364671813276",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-tabulate")
