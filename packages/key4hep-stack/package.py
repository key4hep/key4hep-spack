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
    variant(
        "ml",
        default=True,
        description="add packages that are necessary for ml inference",
    )
    variant(
        "analysis",
        default=True,
        description="Add packages that are useful for analysis",
    )
    variant(
        "full",
        default=False,
        description="Build the full stack regardless of the values of the variants",
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
    depends_on("k4mljettagger", when="+ml")
    depends_on("k4mljettagger", when="+full")
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
    depends_on("fccanalyses~onnx", when="~ml")
    depends_on("fccanalyses+onnx", when="+ml")
    depends_on("fccanalyses+onnx", when="+full")
    depends_on("fccdetectors")
    depends_on("k4reccalorimeter", when="+ml")
    depends_on("k4reccalorimeter", when="+full")

    # ILCSoft packages
    for variant in ("ml", "generators"):
        depends_on(f"ilcsoft +{variant}", when=f"+{variant}")
        depends_on(f"ilcsoft ~{variant}", when=f"~{variant}")
    depends_on("ilcsoft +generators +ml", when="+full")

    for v in ("+generators", "+full"):
        with when(v):
            # Generators
            depends_on("k4generatorsconfig")
            depends_on("evtgen+pythia8+tauola+photos")
            depends_on("herwig3")
            depends_on("lhapdf")
            depends_on("madgraph5amc")
            depends_on("photos+hepmc3")
            depends_on("sherpa")
            # babayaga doesn't build on macOS
            depends_on("babayaga", when="platform=linux")
            depends_on("bhlumi")
            depends_on("whizard")
            depends_on("kkmcee")
            depends_on("guinea-pig")

            depends_on("py-pybdsim")
            depends_on("py-pymadx")
            depends_on("py-pytransport")

    # Basic build and debug tools
    depends_on("autoconf")
    depends_on("automake")
    depends_on("catch2@3:")
    depends_on("cmake")
    depends_on("ninja")
    depends_on("py-pip")
    depends_on("gdb")
    depends_on("libtool")

    for v in ("+devtools", "+full"):
        with when(v):
            # More extensive Devtools
            depends_on("cppcheck")
            depends_on("doxygen")
            depends_on("llvm")
            # depends_on("iwyu") # Not that useful and makes the LLVM built be older than it should
            depends_on("man-db")
            depends_on("mold")
            depends_on("prmon")
            depends_on("py-black")
            depends_on("py-flake8")
            depends_on("py-pylint")
            depends_on("py-boto3")
            depends_on("py-gcovr")
            depends_on("py-pre-commit")
            depends_on("py-ruff")
            depends_on("benchmark")

    for v in ("+analysis", "+full"):
        with when(v):
            # Generic analysis packages
            depends_on("py-awkward")
            depends_on("py-uproot")
            depends_on("py-scipy")
            depends_on("py-pandas")
            depends_on("py-particle")
            depends_on("py-pyhepmc")
            depends_on("py-h5py")
            depends_on("py-ipykernel")
            depends_on("py-ipython")
            depends_on("py-jupytext@1.16:")
            depends_on("py-matplotlib")
            depends_on("py-nbconvert")
            depends_on("py-vector")

    for v in ("+ml", "+full"):
        with when(v):
            # ML inference related stuff
            depends_on("py-onnxruntime")
            depends_on("py-onnx")
            depends_on("py-torch")
            depends_on("py-scikit-learn")
            depends_on("py-xgboost")

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
