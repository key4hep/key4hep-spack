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

    # match signature to different compiler versions
    patch(
        "https://patch-diff.githubusercontent.com/raw/scikit-hep/pyhepmc/pull/85.patch?full_index=1",
        sha256="0a87e2da07fbf12a15b2c7025f7ee3fcd5bff540f331e4d820e4ea0ba2e779f2",
        when="@:2.14.0",
    )

    depends_on("cmake", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("hepmc3", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
    # In v2.14.0 a dot command is run at import time to check which formats are supported
    # The system dot on Alma 9 does not support any formats and importing fails so graphviz is required
    depends_on("graphviz", type="run")

    @run_before("install")
    def use_external_pybind11(self):
        filter_file("(EXTERNAL_PYBIND11.*) OFF", r"\1 ON", "CMakeLists.txt")
