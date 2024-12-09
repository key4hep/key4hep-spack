from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Cepcsw(CMakePackage, Key4hepPackage):
    """CEPC offline experiment software based on Key4hep."""

    homepage = "https://github.com/cepc/CEPCSW"
    url = "https://github.com/cepc/CEPCSW/archive/v0.1.tar.gz"
    git = "https://github.com/cepc/CEPCSW.git"

    maintainers = ["mirguest"]

    version("master", branch="master")
    version(
        "0.2.10",
        sha256="f26f03d5041733e51be529989593ad5ab7be695a49f4b9a5c60194c47949d825",
    )
    version(
        "0.2.9",
        sha256="ce78b740da71cf500766782eca46e86d521af2d94042e803897b0dc7dbb405cd",
    )
    version(
        "0.2.8",
        sha256="b155d079617f1f6514bae7123972ff6ce86f4568eba5d07789500d1a0497c1f8",
    )
    version(
        "0.2.6",
        sha256="4fd46326154a13f89a39ca98d23253542b78de7abac572808fa59f929566e02a",
    )
    version(
        "0.2.5",
        sha256="fb0aa15a3895fe822f936936b810205e9330a9ffe763be16a225fc5e9580bd2c",
    )
    version(
        "0.2.4",
        sha256="86802d09da1feca8fdfaf947ccad762e28dd91644669c1a057ac4df748e807c9",
    )
    version(
        "0.2.3",
        sha256="38254b2beeb8eb6de81e2dfa94b7c9f1b307fe512dc4fec9c3691f359509d008",
    )
    version(
        "0.2.2",
        sha256="634bc0ce54a82ddaac43dd37d504bf1ea390dcdd30f9ebfd2264fc7073e37fea",
    )

    depends_on("clhep")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("podio")
    depends_on("k4fwcore")
    depends_on("garfieldpp")
    depends_on("gaudi")
    depends_on("gear")
    depends_on("genfit")
    depends_on("lcio")
    depends_on("lccontent")
    depends_on("hepmc")
    depends_on("pandorasdk")
    depends_on("pandorapfa")
    depends_on("root")
    depends_on("py-onnxruntime")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append("-DCMAKE_MODULE_PATH=%s" % cmake_modules)
        return args

    def flag_handler(self, name, flags):
        if name == "cxxflags":
            flags.append("-Wno-c++11-narrowing")
        return (flags, None, flags)

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
