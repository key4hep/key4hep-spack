# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymadx(PythonPackage):
    """Utilities for processing and analysing MADX output"""

    homepage = "https://github.com/bdsim-collaboration/pymadx"
    url = "https://github.com/bdsim-collaboration/pymadx/archive/v2.2.1.tar.gz"
    git = "https://github.com/bdsim-collaboration/pymadx.git"

    tags = ["hep"]

    maintainers("jmcarcell")

    version("master", branch="master")

    version(
        "2.2.1",
        sha256="c4109b5b6214c50e1cc6f0ff76c38b3ea88043536a9c3f8b45685b8b3babac97",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-tabulate")
