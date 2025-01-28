# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class K4simdelphes(CMakePackage, Ilcsoftpackage):
    """EDM4HEP output for Delphes."""

    homepage = "https://github.com/key4hep/k4SimDelphes"
    git = "https://github.com/key4hep/k4SimDelphes.git"
    url = "https://github.com/key4hep/k4SimDelphes/archive/v00-00-01.tar.gz"

    maintainers = ["vvolkl", "tmadlener"]

    version("main", branch="main")
    version(
        "00-07-04",
        sha256="dd92de9ec5a680c26e73b4a4b9aa7377b1366bf26ceeb5960fb114671dec1c5e",
    )
    version(
        "00-07-03",
        sha256="1b6fbb9cb921d594798e2344fd03eee3be07b7694105eb918ced6169f1ccfe3b",
    )
    version(
        "00-07-02",
        sha256="bda65916f13b40dc30eb618e0c02b888d70e77a9a080e2f3557c616ef1a995df",
    )
    version(
        "00-07-01",
        sha256="ae0b5e913c78cfe89c89ff5e04c0d46de9235b34dbdf5cb64ca704530e0f6ced",
    )
    version(
        "00-07",
        sha256="c9d2c3dd74c7047461bf13558c1d26aec6e68b5fe73cab513ed1a83f9b1aca57",
    )
    version(
        "00-06-02",
        sha256="20aada60613df12760a1007974f1e1d0a8a248ef7d9c278097934221b08e712f",
    )
    version(
        "00-06-01",
        sha256="662ac032c20837d88a44dc8d09913063ec681322b04a952524b6e7c7e19874e8",
    )
    version(
        "00-06",
        sha256="e83e17c5476a81d9a640a053b03b43f1ada3d4c34c02b30c9e64136f2917f1e7",
    )

    variant("framework", default=True, description="Build Gaudi framework integration.")
    variant(
        "integration_tests",
        default=True,
        description="Enable integration tests for framework.",
    )
    variant(
        "delphes_pythia",
        default=True,
        description="Build standalone executable with Pythia input.",
    )
    variant(
        "delphes_hepmc",
        default=True,
        description="Build standalone executable with Hepmc input.",
    )
    variant(
        "delphes_pythia_evtgen",
        default=True,
        description="Build standalone executable with Pythia+EvtGen input",
    )

    depends_on("edm4hep", type=("build", "link", "run"))
    depends_on("podio")
    depends_on("delphes@3.5.1pre04:", when="@00-03-00:", type=("build", "link", "run"))

    depends_on("pythia8", when="+delphes_pythia")
    depends_on("evtgen+pythia8+tauola+photos", when="+delphes_pythia_evtgen")
    depends_on("hepmc", when="+delphes_hepmc")
    depends_on("hepmc3", when="+framework")
    depends_on("k4fwcore", when="+framework")

    depends_on("catch2@3.0.1:", type=("build", "test"))
    depends_on("k4gen", when="+integration_tests", type=("build", "test", "run"))

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_FRAMEWORK", "framework"),
            self.define_from_variant("BUILD_PYTHIA_READER", "delphes_pythia"),
            self.define_from_variant("BUILD_HEPMC_READER", "delphes_hepmc"),
            self.define_from_variant("BUILD_EVTGEN_READER", "delphes_pythia_evtgen"),
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            "-DUSE_EXTERNAL_CATCH2=ON",
            "-DBUILD_TESTING={0}".format(self.run_tests),
        ]
        return args

    def setup_run_environment(self, env):
        env.set("K4SIMDELPHES", self.prefix.share.k4SimDelphes)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
