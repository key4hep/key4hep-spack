# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Fcalclusterer(CMakePackage, Ilcsoftpackage):
    """Reconstruction for the Forward Calorimeters of Future e+e- colliders."""

    url = "https://github.com/FCalSW/FCalClusterer/archive/v01-00-01.tar.gz"
    homepage = "https://github.com/FCalSW/FCalClusterer"
    git = "https://github.com/FCalSW/FCalClusterer.git"

    maintainers("vvolkl")

    version("master", branch="master")
    version(
        "1.1",
        sha256="4310adaaf8171b8aec544237d957e3f8cd5ca6c8c27af4abd18923685466c51f",
    )
    version(
        "1.0.6",
        sha256="e1fcd34836f3feb2c6788a577f8b507873cfcf1b3b780ecfe3dca553de14f93b",
    )
    version(
        "1.0.5",
        sha256="34c687e9d98c24c92569e2d1e391ef7be731a2800071e823b4359b7e8a5e8194",
    )
    version(
        "1.0.4",
        sha256="048199be72f575abfb3bacddfd84a1870244b861e207efa66dc433c67f62e56b",
    )
    version(
        "1.0.3",
        sha256="5360ccb85f8742d9f4b84c7a3bb3ed3574b534f1b08240100c5b4e48e8ffa35e",
    )
    version(
        "1.0.2",
        sha256="6c6898f8641743a7654b1c1e7b3a52643be9d23f8bb3624e415c51549ac64cbe",
    )
    version(
        "1.0.1",
        sha256="87837d7fd802e46c8530c721035ae75946d699031f093612ec02a7fabe0c6143",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ilcutil")
    depends_on("lcio")
    depends_on("gear")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("root +unuran +math")
    depends_on("dd4hep")

    depends_on("k4geo", type="test")
    depends_on("marlindd4hep", type="test")

    # CMAKE_INSTALL_PREFIX is overwritten by the package
    patch("install.patch", when="@:1.0.1")
    patch("random-shuffle-c17.patch", when="@:1.0.1")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    @run_after("install")
    def install_source(self):
        install_tree(
            ".",
            self.prefix,
            ignore=lambda x: x
            in (
                "README.md",
                "CMakeLists.xt",
                "LICENSE",
                ".clang-format",
                "doc",
            ),
        )

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libFCalClusterer.so")

    def setup_build_environment(self, env):
        # k4_setup_env_for_framework_tests(self.spec, env)
        env.prepend_path(
            "MARLIN_DLL", self.spec["marlindd4hep"].prefix.lib + "/libMarlinDD4hep.so"
        )
        env.prepend_path("ROOT_INCLUDE_PATH", self.spec["dd4hep"].prefix.include)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["dd4hep"].prefix.lib)
        # used p.ex. in ddsim to find DDDetectors dir
        env.set("DD4hepINSTALL", self.spec["dd4hep"].prefix)
        env.set("DD4HEP", self.spec["dd4hep"].prefix.examples)
        env.set("DD4hep_DIR", self.spec["dd4hep"].prefix)
        env.set("DD4hep_ROOT", self.spec["dd4hep"].prefix)
