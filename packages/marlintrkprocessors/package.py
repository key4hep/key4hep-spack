# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlintrkprocessors(CMakePackage, Ilcsoftpackage):
    """A collection of Tracking Relelated Processors Based on MarlinTrk"""

    url = "https://github.com/iLCSoft/MarlinTrkProcessors/archive/v02-11.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinTrkProcessors"
    git = "https://github.com/iLCSoft/MarlinTrkProcessors.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "2.12.7",
        sha256="34cc4cfbf6265fbd9c1164a294957596a5cd722d82d9e66a3f8db51414fa8271",
    )
    version(
        "2.12.6",
        sha256="1414329054b95747a3406a73b2db41b352d322008af68a3e1d7526cf80ac7898",
    )
    version(
        "2.12.5",
        sha256="4f02cbb2aae4ec2bf813312ebb796bd756e9ac130e229174b8de164cf160787d",
    )
    version(
        "2.12.4",
        sha256="3aa29fc3d51767dd73d41fb9991c87eccba40c2b4b8f080779386a994094f08b",
    )
    version(
        "2.12.3",
        sha256="1af8f1536df42a31c4fa45f860710afb61d25683a9ffef4bdf4e6bc204b99dde",
    )
    version(
        "2.12.2",
        sha256="862ed161a882f6b3bc14033be8a38fa9a126594da3774194092adb1c69a0b5e5",
    )
    version(
        "2.12.1",
        sha256="677532d8d7c9a8489be091d249c8893e2bfb66c78d0e1537cafff97456a00bf5",
    )
    version(
        "2.12",
        sha256="ac1a3af380c837868649c8b7767e7641d25a1ecf40690726d55a9bcc58a54640",
    )
    version(
        "2.11",
        sha256="49a567831e2b7a0c43ded955ce31fbe7d467a59960f4bcc2c2120e20762639b0",
    )

    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("dd4hep")
    depends_on("marlintrk")
    depends_on("kitrack")
    depends_on("kitrackmarlin")
    depends_on("gsl")
    depends_on("ddkaltest")
    depends_on("raida")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libMarlinTrkProcessors.so")

    def cmake_args(self):
        return [
            self.define(
                "CMAKE_CXX_STANDARD", self.spec["root"].variants["cxxstd"].value
            )
        ]
