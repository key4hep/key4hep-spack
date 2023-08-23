from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class Fccanalyses(CMakePackage, Key4hepPackage):
    """RDF Analysers for the FCC."""

    homepage = "https://github.com/HEP-FCC/FCCAnalyses"
    git = "https://github.com/HEP-FCC/FCCAnalyses.git"
    url = "https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz"

    maintainers = ["vvolkl", "clementhelsens"]

    version("master", branch="master")

    version(
        "0.7.0",
        sha256="3cc38d623fc5a17dfc41b3ef8a76b42bd2e9d74860a4adafb6e32f282d8a25fa",
    )
    version(
        "0.6.0",
        sha256="a740c1818cc9e02ce44306b9a4f828b3ce85d2afaed1fc06d8f8a41f89f9abe2",
    )
    version(
        "0.5.1",
        sha256="2d5493340e21e8a24cbbfec9a465616fca736c5058bd27acf79eb07f8948ea2b",
    )
    version(
        "0.5.0",
        sha256="6c4b68d15fbae3793473dc4475f216b65c1962ed5de7979e75b024cb6d05d541",
    )
    version(
        "0.4.1",
        sha256="60db645152326775e9ce0f8c5017bd68d83d0024ac71e3266dac2f83d96ffce3",
    )
    version(
        "0.4.0",
        sha256="0089d8dd71e45f31afb531f4bdd3140f78eb5484cc126746fff51d750b317a1f",
    )
    version(
        "0.3.7",
        sha256="523e7c6d8db73028356b468afb01bd1f077ff4268817afe56df92fc47d492fd2",
    )
    version(
        "0.3.6",
        sha256="ec673e22b44c6c7b4e947ba16e3c0f12c08ee4443433fcdfd2c09a6795ddb0b7",
    )
    version(
        "0.3.5",
        sha256="efc08ea107d2fe10c24486d549e8ad8f6457c9c9003d2d12d1c44ebcdbd9664c",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/FCCAnalyses/pull/176.patch",
        when="@0.4.0",
        sha256="bff4be96d0c177caccc3642bc1b3538004a8d3e5a19b472563ac867281a65bd6",
    )

    variant("onnx", default=True, description="Build ONNX-dependent analyzers.")
    variant("acts", default=True, description="Build Acts-dependent analyzers.")
    variant("dd4hep", default=True, description="Build DD4hep-dependent analyzers.")

    generator = "Ninja"

    depends_on("ninja", type="build")
    depends_on("root +tmva+xrootd")
    depends_on("vdt")
    depends_on("fastjet")
    depends_on("python")
    depends_on("edm4hep")
    depends_on("py-awkward@1.4.0", when="@:0.6.0")
    depends_on("acts@6.00.0:19.5.0", when="@0.3.5:0.6.0 +acts")
    depends_on("acts@19.6.0:", when="@0.7.0: +acts")
    depends_on("eigen")
    depends_on("dd4hep", when="+dd4hep")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-onnxruntime", when="+onnx")
    depends_on("delphes@3.5.1pre07:", when="@0.7.0:")

    def cmake_args(self):
        args = [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            ),
            self.define_from_variant("WITH_ACTS", "acts"),
            self.define_from_variant("WITH_DD4HEP", "dd4hep"),
            self.define_from_variant("WITH_ONNX", "onnx"),
        ]
        return args

    # todo: update the cmake config to remove this
    def setup_build_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)  # todo: remove
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["vdt"].prefix.include)

        if self.spec.satisfies("@:0.6.0"):
            python_version = self.spec["python"].version.up_to(2)
            awk_lib_dir = self.spec["py-awkward"].prefix.lib
            awk_pydir = join_path(
                awk_lib_dir,
                "python{0}".format(python_version),
                "site-packages/awkward/include",
            )
            env.prepend_path("CPATH", awk_pydir)
            awk_pydir = join_path(
                awk_lib_dir, "python{0}".format(python_version), "site-packages"
            )
            env.prepend_path("LD_LIBRARY_PATH", awk_pydir)
        k4_setup_env_for_framework_tests(self.spec, env)

    def setup_run_environment(self, env):
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include.FCCAnalyses)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PYTHONPATH", self.prefix.share + '/examples')
        # this should point to share/ by key4hep convention
        #  but we want to make it work with the tutorials
        env.set("FCCANALYSES", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["fccanalyses"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["fccanalyses"].prefix.lib64)
        env.prepend_path("FCCDICTSDIR", "/cvmfs/fcc.cern.ch/FCCDicts")
        if self.spec.satisfies("@:0.6.0"):
            # libawkward.so is in prefix/lib/pythonX.Y/site-packages
            python_version = self.spec["python"].version.up_to(2)
            awk_lib_dir = self.spec["py-awkward"].prefix.lib
            awk_pydir = join_path(
                awk_lib_dir, "python{0}".format(python_version), "site-packages"
            )
            env.prepend_path("CPATH", join_path(awk_pydir, "include"))
            env.prepend_path("LD_LIBRARY_PATH", awk_pydir)

        if self.spec.variants["onnx"].value:
            env.prepend_path("LD_LIBRARY_PATH",
                             self.spec["py-onnxruntime"].prefix.lib)

    # tests need installation, so skip here ...
    def check(self):
        pass

    # ... and  add custom check step that runs after installation instead
    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
