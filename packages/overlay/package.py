# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Overlay(CMakePackage, Ilcsoftpackage):
    """The package Overlay provides code for event overlay with Marlin."""

    url = "https://github.com/iLCSoft/Overlay/archive/v00-22.tar.gz"
    homepage = "https://github.com/iLCSoft/Overlay"
    git = "https://github.com/iLCSoft/Overlay.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "0.22.4",
        sha256="bd770f17e006d0cda99d233b64603c43920350695c1649391197cfe0c53628b2",
    )
    version(
        "0.22.3",
        sha256="4a26b407a9275735c6ae156fdf073cbc6ea820e474d8e5ccc051753429a01ae1",
    )
    version(
        "0.22.2",
        sha256="305bdf568dc5fd221d6bd5d499cc25f7c567cc3ae21ff2954409a66549e4150f",
    )
    version(
        "0.22.1",
        sha256="2f3ca472fe6aae44cdae0553f0e65b3c086a0d887d9cf53fd19468fb6107155b",
    )
    version(
        "0.22",
        sha256="fa03e2870b8f072fd9c1cd68354274437050ce6ed30d0db9a816a3cbdee54cb1",
    )

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("marlinutil")
    depends_on("clhep")
    depends_on("raida")

    def setup_run_environment(self, env):
        env.prepend_path("MARLIN_DLL", self.prefix.lib + "/libOverlay.so")

    def cmake_args(self):
        # C++ Standard
        return ["-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value]
