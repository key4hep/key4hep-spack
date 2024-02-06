# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Gear(CMakePackage, Ilcsoftpackage):
    """Linear Collider Conditions Data toolkit."""

    homepage = "https://github.com/iLCSoft/gear"
    git = "https://github.com/iLCSoft/gear.git"
    url = "https://github.com/iLCSoft/gear/archive/v01-05.tar.gz"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.9.2",
        sha256="7ea9e13046aef53f12e4071e9937378c93f17fe70f8b673e91bbc3a81385742d",
    )
    version(
        "1.9.1",
        sha256="75f7123cb5136fe1bd504c4c08816a37e8c6faaf090e30df0497f9ec9aa56d21",
    )
    version(
        "1.9.0",
        sha256="18564d50bc4863441bd4b5b72dda565065f8b7f5821e30c804c7e93c7afe84ae",
    )

    patch("build_testing.patch", when="@1.9.0")

    variant("tgeo", default=True, description="builds with ROOT tgeo")

    variant("doc", default=False, description="build doxygen documentation")

    depends_on("ilcutil")
    depends_on("clhep")

    depends_on("root", when="+tgeo")
    depends_on("doxygen", when="+doc")

    depends_on("root", type="test")

    def cmake_args(self):
        args = []
        args.append(self.define("BUILD_TESTING", self.run_tests))
        args.append(self.define_from_variant("GEAR_TGEO", "tgeo"))
        args.append(self.define_from_variant("INSTALL_DOC", "doc"))
        args.append("-DCMAKE_CXX_STANDARD=17")
        return args
