# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Conformaltracking(CMakePackage, Ilcsoftpackage):
    """Package for running pattern recognition based on conformal mapping
    and cellular automaton. This is not tied to a given geometry, but
    has been developed for the CLIC detector model 2015."""

    homepage = "https://github.com/iLCSoft/ConformalTracking/"
    url = "https://github.com/iLCSoft/ConformalTracking/archive/v01-10.tar.gz"
    git = "https://github.com/iLCSoft/ConformalTracking.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.12",
        sha256="e586bbae21e49a69797109dd9db267812e9ded1cd98877f245972a329cea9cc5",
    )
    version(
        "1.11.1",
        sha256="af7a369d38df00f07d7e6f13c631937393bac667b91022cad043d94ffb9e9fac",
    )
    version(
        "1.11",
        sha256="297790748e211c7c8e52d70a283d6a9477ea0318db6c8521e640d41e4006520a",
    )
    version(
        "1.10",
        sha256="7e0f5774a0ea80147b67db6c218de6001e83e46abc14396564a0a552725dbcce",
    )
    version(
        "1.9", sha256="c9ae5bd4f833b4542c8e2df01698c1a40ed8bdfc7330eb0e06ec9c3304b2bbca"
    )
    version(
        "1.8", sha256="e25d2a5df0e77a4223120b0697e2c2414b6ffd12fe6f645c2fbb1a372b635c31"
    )

    depends_on("ilcutil")
    depends_on("root")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("marlintrk")
    depends_on("raida")
    depends_on("boost")

    def setup_run_environment(self, spack):
        spack.prepend_path("MARLIN_DLL", self.prefix.lib + "/libConformalTracking.so")

    def cmake_args(self):
        # C++ Standard
        return ["-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value]
