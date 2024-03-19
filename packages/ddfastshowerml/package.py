# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ddfastshowerml(CMakePackage, Ilcsoftpackage):
    """Linear Collider framework"""

    homepage = "https://gitlab.desy.de/ilcsoft/ddfastshowerml"
    git = "https://gitlab.desy.de/ilcsoft/ddfastshowerml.git"
    url = "https://gitlab.desy.de/ilcsoft/ddfastshowerml"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    variant("inference", values=("onnxruntime", "torch", "both"), default="both")

    depends_on("py-onnxruntime", when="inference=onnxruntime")
    depends_on("py-onnxruntime", when="inference=both")
    depends_on("py-torch", when="inference=torch")
    depends_on("py-torch", when="inference=both")
    depends_on("dd4hep")

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args
