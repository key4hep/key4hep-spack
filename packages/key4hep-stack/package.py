from datetime import datetime
import os

# import common methods for use in recipe from common.py
# (so other recipe can import from spack.pkg.k4.key4hep_stack)
# (which is the most convenient way to make that code available
#  without creation of a new module
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from common import *


class Key4hepStack(BundlePackage, Key4hepPackage):
    """Bundle package to install the Key4hep software stack."""

    homepage = "https://cern.ch/key4hep"

    version("master")
    version(datetime.today().strftime("%Y-%m-%d"))

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ["install"]

    variant(
        "devtools",
        default=True,
        description="add tools necessary for software development to the stack",
    )
    variant(
        "generators",
        default=True,
        description="add some standalone generators to the stack",
    )

    # Fake variant that does nothing but this lets us group the packages
    # that are build with Debug mode
    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug"),
        description="Build type",
    )

    # Add compilers to the build dependencies
    # so that we have them available to set them in the env script
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # Key4hep packages
    depends_on("cldconfig")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("k4mljettagger")
    depends_on("k4clue")
    depends_on("k4edm4hep2lcioconv")
    depends_on("k4fwcore")
    depends_on("k4gaudipandora")
    depends_on("k4gen")
    depends_on("k4projecttemplate")
    depends_on("k4reco")
    depends_on("k4rectracker")
    depends_on("k4simdelphes")
    depends_on("k4simgeant4")
    depends_on("k4geo")
    depends_on("podio")
    # HEP-FCC packages
    depends_on("fcc-config")
    depends_on("fccsw")
    depends_on("dual-readout")
    depends_on("fccanalyses")
    depends_on("fccdetectors")
    depends_on("k4reccalorimeter")
    # ILCSoft packages
    depends_on("ilcsoft")

    # Generators
    depends_on("k4generatorsconfig", when="+generators")
    depends_on("evtgen+pythia8+tauola+photos", when="+generators")
    depends_on("herwig3", when="+generators")
    depends_on("lhapdf", when="+generators")
    depends_on("madgraph5amc", when="+generators")
    depends_on("photos+hepmc3", when="+generators")
    depends_on("sherpa", when="+generators")
    # babayaga doesn't build on macOS
    depends_on("babayaga", when="+generators platform=linux")
    depends_on("bhlumi", when="+generators")
    depends_on("whizard", when="+generators")
    depends_on("kkmcee", when="+generators")
    depends_on("guinea-pig", when="+generators")

    depends_on("py-pybdsim", when="+generators")
    depends_on("py-pymadx", when="+generators")
    depends_on("py-pytransport", when="+generators")

    # Devtools
    depends_on("autoconf", when="+devtools")
    depends_on("automake", when="+devtools")
    depends_on("catch2@3:", when="+devtools")
    depends_on("cmake", when="+devtools")
    depends_on("cppcheck", when="+devtools")
    depends_on("doxygen", when="+devtools")
    depends_on("gdb", when="+devtools")
    depends_on("libtool", when="+devtools")
    depends_on("llvm", when="+devtools")
    # depends_on("iwyu", when="+devtools") # Not that useful and makes the LLVM built be older than it should
    depends_on("man-db", when="+devtools")
    depends_on("mold", when="+devtools")
    depends_on("ninja", when="+devtools")
    depends_on("prmon", when="+devtools")
    depends_on("py-awkward", when="+devtools")
    depends_on("py-black", when="+devtools")
    depends_on("py-flake8", when="+devtools")
    depends_on("py-pylint", when="+devtools")
    depends_on("py-boto3", when="+devtools")
    depends_on("py-gcovr", when="+devtools")
    depends_on("py-pyhepmc", when="+devtools")
    depends_on("py-h5py", when="+devtools")
    depends_on("py-ipykernel", when="+devtools")
    depends_on("py-ipython", when="+devtools")
    depends_on("py-jupytext@1.16:", when="+devtools")
    depends_on("py-matplotlib", when="+devtools")
    depends_on("py-nbconvert", when="+devtools")
    depends_on("py-onnxruntime", when="+devtools")
    depends_on("py-onnx", when="+devtools")
    depends_on("py-pandas", when="+devtools")
    depends_on("py-particle", when="+devtools")
    depends_on("py-pip", when="+devtools")
    depends_on("py-pre-commit", when="+devtools")
    depends_on("py-ruff", when="+devtools")
    depends_on("py-scikit-learn", when="+devtools")
    depends_on("py-scipy", when="+devtools")
    depends_on("py-torch", when="+devtools")
    depends_on("py-uproot", when="+devtools")
    depends_on("py-vector", when="+devtools")
    depends_on("py-xgboost", when="+devtools")
    depends_on("benchmark", when="+devtools")

    # Other
    depends_on("acts")
    depends_on("aprilcontent")
    depends_on("bdsim")
    depends_on("cluestering")
    depends_on("delphes")
    depends_on("geant4")
    # depends_on('k4actstracking')
    depends_on("python")
    depends_on("xrootd")
    # depends_on("cepcsw") # cepcsw depends on garfieldpp and genfit
    depends_on("garfieldpp")
    depends_on("genfit")
    depends_on("opendatadetector")
    depends_on("sdhcalcontent")

    def setup_run_environment(self, env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        env.set("LC_ALL", "C")
        env.set("KEY4HEP_STACK", os.path.join(self.spec.prefix, "setup.sh"))

        # set vdt, needed for root, see https://github.com/spack/spack/pull/37278
        if "vdt" in self.spec:
            env.prepend_path("CPATH", self.spec["vdt"].prefix.include)
            # When building podio with +rntuple there are warnings constantly without this
            env.prepend_path("LD_LIBRARY_PATH", self.spec["vdt"].libs.directories[0])

        if "whizard" in self.spec:
            # Otherwise whizard generated libraries will not be able to find libomega.so
            env.prepend_path(
                "LD_LIBRARY_PATH", self.spec["whizard"].libs.directories[0]
            )

        # See https://github.com/root-project/root/issues/18949
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["vc"].prefix.include)

        # Don't use libtools from the system
        if "libtool" in self.spec:
            env.prepend_path("PATH", self.spec["libtool"].prefix.bin)
            env.prepend_path("LD_LIBRARY_PATH", self.spec["libtool"].prefix.lib)

        if "autoconf" in self.spec:
            env.prepend_path("PATH", self.spec["autoconf"].prefix.bin)
        if "automake" in self.spec:
            env.prepend_path("PATH", self.spec["automake"].prefix.bin)

        # Add the correct path in pytorch to CMAKE_PREFIX_PATH
        # This could be deleted (to be tested) once https://github.com/spack/spack/pull/49267 is merged
        if "py-torch" in self.spec:
            env.prepend_path(
                "CMAKE_PREFIX_PATH", self.spec["py-torch"].package.cmake_prefix_paths[0]
            )

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, "K4_LATEST_SETUP_PATH")
