# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytransport(PythonPackage):
    """A Python based converter for TRANSPORT files to BDSIM readable gmad files"""

    homepage = "https://github.com/bdsim-collaboration/pytransport"
    url = "https://github.com/bdsim-collaboration/pytransport/archive/v2.0.2.tar.gz"
    git = "https://github.com/bdsim-collaboration/pytransport.git"

    tags = ["hep"]

    maintainers("jmcarcell")

    version("master", branch="master")

    version(
        "2.0.2",
        sha256="5e858ec0a73695ca8ba62f221e57ed4c5182ded125372e997918a140072b5852",
    )

    depends_on("py-setuptools", type="build")

    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-scipy")
