# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyg4ometry(PythonPackage):
    """Geometry package for high energy physics (Geant4, Fluka)"""

    homepage = "https://bitbucket.org/jairhul/pyg4ometry.git"
    url = "https://bitbucket.org/jairhul/pyg4ometry.git"
    git = "https://bitbucket.org/jairhul/pyg4ometry.git"

    tags = ["hep"]

    maintainers("vvolkl")

    version("master", branch="develop")

    depends_on("python@3.6:")

    depends_on("py-pybind11")
    depends_on("cgal")
    depends_on("py-cython")
    depends_on("py-sympy")
    depends_on("py-ipython")
    depends_on("py-networkx")

    depends_on("vtk+python")
    depends_on("py-pandas")
    depends_on("py-configparser")
    depends_on("py-antlr4-python3-runtime")
    depends_on("py-gitpython")
    depends_on("py-six")
    depends_on("py-fixtures")
    depends_on("py-pbr")
    depends_on("py-traceback2")
    depends_on("py-unittest2")
    depends_on("py-mpmath")
    depends_on("py-wheel")
    depends_on("py-setuptools")
    depends_on("py-pillow")
    depends_on("py-cycler")
    depends_on("py-certifi")
    depends_on("py-gitdb")
    depends_on("py-python-dateutil")
    depends_on("py-pytz")
    depends_on("py-decorator")
    depends_on("py-kiwisolver")
    depends_on("py-pyparsing")
    depends_on("py-pexpect")
    depends_on("py-linecache2")
    depends_on("py-argparse")
    depends_on("py-smmap")
