# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Ddfastshowerml(CMakePackage, Key4hepPackage):
    """Package with utilities and plugins that allow to run fast simulation in Geant4 from ML inference within ddsim (DDG4)"""

    homepage = "https://github.com/key4hep/DDML"
    git = "https://github.com/key4hep/DDML.git"
    url = "https://github.com/key4hep/DDML/archive/refs/tags/v0.2.0.tar.gz"

    maintainers("jmcarcell", "tmadlener")

    version("main", branch="main")
    version(
        "0.2.0",
        sha256="377f34a341bcd11a177195b795c763c98f06450445839982c96adee76f51ad08",
    )
    version(
        "0.1.1",
        sha256="0c11f84a912c89404de46df9ed6f0f0bb4f8985a292f0400f1c4f1b0afea1f72",
    )
    version(
        "0.1.0",
        sha256="17ccdd7673780bbe91d98fe6ad3d9c2ad21803ca71b75b740a6beb0f8ea39358",
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
