# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class DualReadout(CMakePackage, Key4hepPackage):
    """Repository for GEANT4 simulation & analysis of the dual-readout calorimeter"""

    url = "https://github.com/HEP-FCC/dual-readout/archive/v0.0.2.tar.gz"
    homepage = "https://github.com/HEP-FCC/dual-readout"
    git = "https://github.com/HEP-FCC/dual-readout.git"

    maintainers = ["vvolkl", "SanghyunKo"]

    version("master", branch="master")

    version(
        "0.1.5",
        sha256="65a5b0cce56d1eabfbc108edc89eb0795465ff895cb54b553098010a76b1afb6",
    )
    version(
        "0.1.4",
        sha256="fca86bd8e2ab922957babbfcaeb902fda09205ddd23cb1f85b7659b79b205d53",
    )
    version(
        "0.1.3",
        sha256="befaf3b0a66e14f4c4d6a2f09e6884f8c5e1e9f3fbe7bde47212e3aa79a5cbef",
    )
    version(
        "0.1.2",
        sha256="a40db5793089ee5768d45e1a0fd23c821a25f9c68e6330f23a872421f06b8ad2",
    )
    version(
        "0.1.1",
        sha256="8d856b47b0b834ac0a53920434da210639c55a1ef375f7e0341731ad14a25318",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/dual-readout/pull/40.patch?full_index=1",
        sha256="9ff1cad595e631336f49c2430e147f29ddedb5e3eee650c36f9147f420f62423",
        when="@0.1.3 %gcc@14",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/dual-readout/pull/42.patch?full_index=1",
        sha256="8dbe67f968eb81a07820b4e6758ace0d5170a35ccfd896440187160988bc6c79",
        when="@0.1.4",
    )

    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("geant4")
    depends_on("podio")
    depends_on("fastjet")
    depends_on("root")
    depends_on("pythia8")
    depends_on("hsf-cmaketools")
    depends_on("k4fwcore")
    depends_on("simsipm")
    depends_on("k4gen", type="run")
    depends_on("gaudi")

    # Compile with GCC 14
    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/dual-readout/pull/40.patch?full_index=1",
        when="@0.1.3 %gcc@14:",
        sha256="9ff1cad595e631336f49c2430e147f29ddedb5e3eee650c36f9147f420f62423",
    )

    def cmake_args(self):
        args = []
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        return args

    def setup_build_environment(self, env):
        env.set("PYTHIA8_ROOT_DIR", self.spec["pythia8"].prefix)

    def setup_run_environment(self, env):
        env.set("DUALREADOUT", self.spec.prefix)
