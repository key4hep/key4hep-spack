# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPytransport(PythonPackage):
    """A Python based converter for TRANSPORT files to BDSIM readable gmad files"""

    homepage = "https://bitbucket.org/jairhul/pytransport"
    url = "https://bitbucket.org/jairhul/pytransport"
    git = "https://bitbucket.org/jairhul/pytransport.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version("master", branch="master")

    depends_on("py-setuptools", type="build")

    depends_on("py-matplotlib@3:")
    depends_on("py-numpy@1.14:")
    depends_on("py-importlib-metadata")
    depends_on("py-scipy")
