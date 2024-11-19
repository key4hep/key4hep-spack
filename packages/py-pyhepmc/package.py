# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPyhepmc(PythonPackage):
    """Python bindings for HepMC3"""

    homepage = "https://github.com/scikit-hep/pyhepmc"
    url = "https://github.com/scikit-hep/pyhepmc/archive/refs/tags/v2.14.0.tar.gz"
    git = "https://github.com/scikit-hep/pyhepmc.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    version(
        "2.14.0",
        sha256="cb20976b017edd7456492134243faf5d3091c6b9fa52bcc5c3ac6e7c6912fe52",
    )

    depends_on("cmake", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-importlib-resources", type=("build", "run"))

    depends_on("hepmc3")
    depends_on("py-numpy@1.21:")
