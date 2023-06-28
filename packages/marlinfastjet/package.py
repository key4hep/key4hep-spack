# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinfastjet(CMakePackage, Ilcsoftpackage):
    """Marlin processor to interface FastJet."""

    url = "https://github.com/iLCSoft/MarlinFastjet/archive/v00-05-02.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinFastjet"
    git = "https://github.com/iLCSoft/MarlinFastjet.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "0.5.3",
        sha256="bf88cdcea89bb5febe5e77176164ec0d1d0d61be2890978f66a7638ac248ef5b",
    )
    version(
        "0.5.2",
        sha256="abdffa6c2c9328bb094456f6003920d0c860e7faa5c76aea650da9e47e698bdf",
    )

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("fastjet")
    depends_on("fjcontrib")
    depends_on("root")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libMarlinFastJet.so")
