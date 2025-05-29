# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Ddfastshowerml(CMakePackage, Key4hepPackage):
    """Package with utilities and plugins that allow to run fast simulation in Geant4 from ML inference within ddsim (DDG4)"""

    homepage = "https://gitlab.desy.de/ilcsoft/ddfastshowerml"
    git = "https://gitlab.desy.de/ilcsoft/ddfastshowerml.git"
    url = "https://gitlab.desy.de/ilcsoft/ddfastshowerml/-/archive/v0.1.0/ddfastshowerml-v0.1.0.tar.gz"

    maintainers("jmcarcell", "tmadlener")

    version("main", branch="main")
    version(
        "0.2.0",
        sha256="1a124c9d19efe1a5435f8838a31c4d9325e23d0bab7d46603f3de654a4cfbbfd",
    )
    version(
        "0.1.1",
        sha256="a9628624736baea4261950615b698c9389763c18953c29bb5b1635d8d2dd9c3b",
    )
    version(
        "0.1.0",
        sha256="a9628624736baea4261950615b698c9389763c18953c29bb5b1635d8d2dd9c3b",
    )

    variant("inference", values=("onnxruntime", "torch", "both"), default="both")

    depends_on("py-onnxruntime", when="inference=onnxruntime")
    depends_on("py-onnxruntime", when="inference=both")
    depends_on("py-torch", when="inference=torch")
    depends_on("py-torch", when="inference=both")
    depends_on("dd4hep")
    depends_on("openmpi", when="@0.1.1:")

    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
        ]
        # This fixes issues in Ubuntu24 when it's not linking to libgomp from gcc-runtime
        if self.spec.satisfies("inference=torch") or self.spec.satisfies(
            "inference=both"
        ):
            args.append(f"-DCMAKE_SHARED_LINKER_FLAGS={self.compiler.openmp_flag}")
        return args
