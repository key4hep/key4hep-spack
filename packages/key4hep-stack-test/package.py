from datetime import datetime
import os

# import common methods for use in recipe from common.py
# (so other recipe can import from spack.pkg.k4.key4hep_stack)
# (which is the most convenient way to make that code available
#  without creation of a new module
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key4hep-stack'))
from common import *


class Key4hepStackTest(BundlePackage, Key4hepPackage):
    """Bundle package to install the Key4hep software stack (test version)."""

    homepage = "https://cern.ch/key4hep"

    ##################### versions ########################
    #######################################################
    ###  nightly builds
    version("master")
    # this version can be extended with additional version
    # fields to differentiate it, like 'master-2020-10-10'
    #
    ### stable builds
    # builds the latest release of each package
    # the preferred usage is to use the date as version, like:
    version(datetime.today().strftime("%Y-%m-%d"))
    # version('2020-10-06') # example, no need to add here.
    # more complex version configurations should be added in an
    # environment

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ["install"]

    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
    )

    # depends_on("")

    def setup_run_environment(self, env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        env.set("LC_ALL", "C")
        env.set("KEY4HEP_STACK", os.path.join(self.spec.prefix, "setup.sh"))

        # this fixes loading the local emacs, see https://github.com/key4hep/key4hep-spack/issues/486
        env.unset("XDG_DATA_DIRS")

        # set vdt, needed for root, see https://github.com/spack/spack/pull/37278
        if "vdt" in self.spec:
            env.prepend_path("CPATH", self.spec["vdt"].prefix.include)

        # remove when https://github.com/spack/spack/pull/37881 is merged
        if "podio" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["podio"].libs.directories[0])
        if "edm4hep" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["edm4hep"].libs.directories[0])
        if "lcio" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["lcio"].libs.directories[0])

        # remove when https://github.com/spack/spack/pull/38015 is merged
        if "dd4hep" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["dd4hep"].prefix.lib)
            env.prepend_path("LD_LIBRARY_PATH", self.spec["dd4hep"].prefix.lib64)

        # remove when https://github.com/spack/spack/pull/38407 is merged
        if "edm4hep" in self.spec:
            env.prepend_path("PYTHONPATH", self.spec["edm4hep"].prefix.python)

        # Issue on ubuntu, whizard fails to load libomega.so.0
        if self.compiler.operating_system == "ubuntu22.04":
            if "whizard" in self.spec:
                env.prepend_path(
                    "LD_LIBRARY_PATH", self.spec["whizard"].libs.directories[0]
                )

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, "K4_LATEST_SETUP_PATH")
