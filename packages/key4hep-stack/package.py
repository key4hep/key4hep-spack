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

    depends_on("acts")
    # babayaga doesn't build on macOS
    depends_on("babayaga", when="platform=linux")
    depends_on("bdsim")
    depends_on("bhlumi")
    depends_on("cldconfig")
    depends_on("dd4hep")
    depends_on("delphes")
    depends_on("edm4hep")
    depends_on("fcc-config")
    depends_on("geant4")
    depends_on("guinea-pig")
    # depends_on('k4actstracking')
    depends_on("k4mljettagger")
    depends_on("k4clue")
    depends_on("k4edm4hep2lcioconv")
    depends_on("k4fwcore")
    depends_on("k4gaudipandora")
    depends_on("k4gen")
    depends_on("k4projecttemplate")
    depends_on("k4reco")
    depends_on("k4simdelphes")
    depends_on("k4simgeant4")
    depends_on("kkmcee")
    depends_on("k4geo")
    depends_on("podio")
    depends_on("python")
    depends_on("whizard")
    depends_on("xrootd")

    depends_on("k4generatorsconfig", when="+generators")
    depends_on("evtgen+pythia8+tauola+photos", when="+generators")
    depends_on("herwig3", when="+generators")
    depends_on("lhapdf", when="+generators")
    depends_on("madgraph5amc", when="+generators")
    depends_on("photos+hepmc3", when="+generators")
    # Sherpa3
    depends_on("sherpa", when="+generators")
    depends_on("sherpa2", when="+generators")

    depends_on("py-pybdsim", when="+generators")
    depends_on("py-pymadx", when="+generators")
    depends_on("py-pytransport", when="+generators")

    depends_on("ilcsoft")

    depends_on("fccsw")
    depends_on("dual-readout")
    depends_on("fccanalyses")
    depends_on("fccdetectors")
    depends_on("k4reccalorimeter")
    depends_on("k4rectracker")

    # depends_on("cepcsw") # cepcsw depends on garfieldpp and genfit
    depends_on("garfieldpp")
    depends_on("genfit")

    depends_on("opendatadetector")

    depends_on("catch2@3:", when="+devtools")
    depends_on("cmake", when="+devtools")
    depends_on("doxygen", when="+devtools")
    depends_on("gdb", when="+devtools")
    depends_on("llvm", when="+devtools")
    # depends_on("iwyu", when="+devtools") # Not that useful and makes the LLVM built be older than it should
    depends_on("man-db", when="+devtools")
    depends_on("ninja", when="+devtools")
    # depends_on('prmon', when='+devtools')
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
    depends_on("py-xgboost", when="+devtools")
    depends_on("benchmark", when="+devtools")

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

        # Issue on ubuntu, whizard fails to load libomega.so.0
        if (
            self.compiler.operating_system == "ubuntu22.04"
            or self.compiler.operating_system == "ubuntu24.04"
        ):
            env.prepend_path(
                "LD_LIBRARY_PATH", self.spec["whizard"].libs.directories[0]
            )

        # When changing CMAKE_INSTALL_LIBDIR to lib, everything is installed to
        # <root>/lib, instead of <root>/lib/root which is the path that is set
        # in the recipe
        # ROOT needs to be in LD_LIBRARY_PATH to prevent using system installations
        env.prepend_path("LD_LIBRARY_PATH", self.spec["root"].prefix.lib)
        env.prepend_path("PYTHONPATH", self.spec["root"].prefix.lib)

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
                "CMAKE_PREFIX_PATH",
                join_path(
                    self["py-torch"].module.python_platlib, "torch", "share", "cmake"
                ),
            )

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, "K4_LATEST_SETUP_PATH")
