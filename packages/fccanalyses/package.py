from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class Fccanalyses(CMakePackage, Key4hepPackage):
    """RDF Analysers for the FCC."""

    homepage = "https://github.com/HEP-FCC/FCCAnalyses"
    git = "https://github.com/HEP-FCC/FCCAnalyses.git"
    url = "https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz"

    maintainers = ["vvolkl", "clementhelsens", "jsmiesko"]

    version("master", branch="master")

    version(
        "0.9.0",
        sha256="205332e02051039878c026abb7e1d9005fe9f89c1c9d27d575531f006a113570",
    )
    version(
        "0.8.0",
        sha256="603ce7f506b706390dd9376c0a7c088b57879de632aaa4152e63e631eecaf95e",
    )
    version(
        "0.7.0",
        sha256="3cc38d623fc5a17dfc41b3ef8a76b42bd2e9d74860a4adafb6e32f282d8a25fa",
    )
    version(
        "0.6.0",
        sha256="a740c1818cc9e02ce44306b9a4f828b3ce85d2afaed1fc06d8f8a41f89f9abe2",
    )

    patch(
        "https://github.com/HEP-FCC/FCCAnalyses/commit/f645584b81aacd0b0f8141b28bcbfa139aecad5c.patch?full_index=1",
        when="@0.8.0",
        sha256="0a324f913e515c0a12d3d799e4c924ad57eaad51cbeae2633417bb819d97d227",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/FCCAnalyses/pull/373.patch?full_index=1",
        sha256="e77e5962d35d764cae5757f066eecc30fa9c60cb05ff087e684636e7c8e4724d",
        when="@:0.9.0 ^py-onnxruntime@1.17.1:",
    )

    patch(
        "https://patch-diff.githubusercontent.com/raw/HEP-FCC/FCCAnalyses/pull/374.patch?full_index=1",
        sha256="aba8cb69ba3494fe48bc4a3d26189932c4974c0013278081893cfef09606fae2",
    )

    variant("onnx", default=True, description="Build ONNX-dependent analyzers.")
    variant("acts", default=False, description="Build Acts-dependent analyzers.")
    variant("dd4hep", default=True, description="Build DD4hep-dependent analyzers.")

    generator = "Ninja"

    depends_on("ninja", type="build")
    depends_on("root +tmva+xrootd")
    depends_on("vdt")
    depends_on("fastjet")
    depends_on("python")
    depends_on("edm4hep")
    depends_on("py-awkward@1.4.0", when="@:0.6.0")
    depends_on("acts", when="+acts")
    depends_on("acts@:29", when="@:0.8.0 +acts")
    depends_on("acts@19.6.0:28", when="@0.7.0 +acts")
    depends_on("acts@6.00.0:19.5.0", when="@:0.6.0 +acts")
    depends_on("eigen")
    depends_on("dd4hep", when="+dd4hep")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-onnxruntime", when="+onnx")
    depends_on("delphes@3.5.1pre07:", when="@0.7.0:")
    depends_on("catch2@3:", type=("test"))

    def cmake_args(self):
        args = [
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define_from_variant("WITH_ACTS", "acts"),
            self.define_from_variant("WITH_DD4HEP", "dd4hep"),
            self.define_from_variant("WITH_ONNX", "onnx"),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        return args

    # todo: update the cmake config to remove this
    def setup_build_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)  # todo: remove
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["vdt"].prefix.include)
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["edm4hep"].prefix.include)

        if "delphes" in self.spec:
            env.set("DELPHES_DIR", self.spec["delphes"].prefix)

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
        # k4_setup_env_for_framework_tests(self.spec, env)

    def setup_run_environment(self, env):
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include.FCCAnalyses)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("PYTHONPATH", self.prefix.share + "/examples")
        # this should point to share/ by key4hep convention
        #  but we want to make it work with the tutorials
        env.set("FCCANALYSES", self.prefix.python)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["fccanalyses"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["fccanalyses"].prefix.lib64)
        env.set("FCCDICTSDIR", "/cvmfs/fcc.cern.ch/FCCDicts")
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
            env.prepend_path("LD_LIBRARY_PATH", self.spec["py-onnxruntime"].prefix.lib)
            env.prepend_path(
                "LD_LIBRARY_PATH", self.spec["py-onnxruntime"].prefix.lib64
            )

    # tests need installation, so skip here ...
    def check(self):
        pass

    # ... and add custom check step that runs after installation instead
    @run_after("install")
    def install_check(self):
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja("test")
