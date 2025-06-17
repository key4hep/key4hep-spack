#!/usr/bin/env python3

from datetime import datetime

from spack.pkg.k4.key4hep_stack import Key4hepPackage, install_setup_script

from common import *


class Key4hepExternalStack(BundlePackage, Key4hepPackage):
    """Bundle package that contains a basic external software stack upon which
    Key4hep can be built

    The packages in this base stack are mainly
    """

    homepage = "https://cern.ch/key4hep"

    version(datetime.today().strftime("%Y-%m-%d"))

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ["install"]

    # Add compilers to the build dependencies
    # so that we have them available to set them in the env script
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # Some generally useful development tools
    depends_on("cmake")
    depends_on("ninja")
    depends_on("python")
    depends_on("gdb")
    depends_on("catch2@3:")
    depends_on("boost")
    depends_on("py-pytest")

    # general hep packages
    depends_on("root")
    depends_on("geant4")
    depends_on("pythia8")
    depends_on("hepmc3")
    depends_on("evtgen +photos+tauola+pythia8+hepmc3")
    depends_on("heppdt")
    depends_on("fastjet")

    # podio dependencies
    depends_on("py-pyyaml")
    depends_on("py-tabulate")
    depends_on("py-jinja2")
    depends_on("py-graphviz")

    # other general deps
    depends_on("py-numpy")
    depends_on("py-scipy")

    # gaudi dependencies
    depends_on("cppgsl")
    depends_on("fmt")
    depends_on("cppunit")
    depends_on("gperftools")
    depends_on("py-networkx")
    depends_on("py-six")
    depends_on("range-v3")
    depends_on("py-pytest-cov")
    depends_on("jemalloc")
    depends_on("aida")

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, "K4_EXTERNAL_STACK")
