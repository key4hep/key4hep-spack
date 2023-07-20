# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4simdelphes(CMakePackage, Ilcsoftpackage):
    """EDM4HEP output for Delphes."""

    homepage = "https://github.com/key4hep/k4SimDelphes"
    git = "https://github.com/key4hep/k4SimDelphes.git"
    url = "https://github.com/key4hep/k4SimDelphes/archive/v00-00-01.tar.gz"

    maintainers = ["vvolkl", "tmadlener"]

    version("main", branch="main")
    version(
        "00-05",
        sha256="a2964d674c017cfe4d3bf38ed3899c6eda8a5d1baef2e1d122ed21fad2a551b8",
    )
    version(
        "00-04",
        sha256="4f5c718cf646ff31cf9f9803fbf77d74cdf5ba5762a15096cf48c71830c7a94b",
    )
    version(
        "00-03-01",
        url="https://github.com/key4hep/k4SimDelphes/archive/v00-03-01.tar.gz",
        sha256="b4d441225ca2bef8f2c506baeb16ef7b0e5117dabc38f8028009e7cfa3e21a8a",
    )
    version(
        "00-03-00",
        url="https://github.com/key4hep/k4SimDelphes/archive/v00-03-00.tar.gz",
        sha256="f2dc577738a3819b33b23ee829a1123f283293512a09c62de166d95e55232776",
    )
    version(
        "00-02-01",
        sha256="2a8fc1ce97fcdbafc0af0b1e13df8005695f92bffe8f0029be952ec6a9eeeb76",
    )
    version(
        "00-02",
        sha256="ffef851a6726b401ac43a7195d76a4d918ea135795eb1b5baff041c7f10ab105",
    )
    version(
        "00-01-09",
        sha256="4f91742f0be9bdb01f25ab8ee9c6650267f8a1b587762cb4cc10aacd16dc30f3",
    )
    version(
        "00-01-08",
        sha256="a9c8dea6b2fd4bf81ad3421f12d1ce43f487a922e0533a832f459f6b3435f7d2",
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

    depends_on("edm4hep@0.5:", when="@00-01-09:", type=("build", "link", "run"))
    depends_on("edm4hep", type=("build", "link", "run"))
    depends_on("podio@0.16:", when="@00-02:", type=("build", "link", "run"))
    depends_on("podio", type=("build", "link", "run"))
    depends_on("delphes@3.5:", when="@00-01-08", type=("build", "link", "run"))
    depends_on("delphes@3.5.1pre02:", when="@00-01-09:", type=("build", "link", "run"))
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
            "-DUSE_EXTERNAL_CATCH2=ON",
            "-DBUILD_TESTING={0}".format(self.run_tests),
        ]
        return args

    def setup_run_environment(self, env):
        env.set("K4SIMDELPHES", self.prefix.share.k4SimDelphes)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_build_environment(self, env):
        k4_setup_env_for_framework_tests(self.spec, env)
