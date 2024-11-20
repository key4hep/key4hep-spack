# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyPyhepmc(PythonPackage):
    """Python bindings for HepMC3"""

    homepage = "https://github.com/scikit-hep/pyhepmc"
    pypi = "pyhepmc/pyhepmc-2.14.0.tar.gz"
    git = "https://github.com/scikit-hep/pyhepmc.git"

    tags = ["hep"]

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    version(
        "2.14.0",
        sha256="17a6f941e4fa06d08a628990f6816d1da5e545d65f533e6f598740d2cb76ace4",
    )

    depends_on("cmake", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("hepmc3", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
    depends_on("graphviz", type="run")

    @run_before("install")
    def use_external_pybind11(self):
        filter_file("(EXTERNAL_PYBIND11.*) OFF", r"\1 ON", "CMakeLists.txt")
