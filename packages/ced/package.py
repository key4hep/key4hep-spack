# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ced(CMakePackage, Ilcsoftpackage):
    """CED is a server client application for OpenGL drawing"""

    homepage = "https://github.com/iLCSoft/CED"
    url = "https://github.com/iLCSoft/CED/archive/v01-09-03.tar.gz"
    git = "https://github.com/iLCSoft/CED.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.10",
        sha256="c3c6540559c00d55bd5981816d39290dbb9b091e34673e301e42934988a74012",
    )
    version(
        "1.9.4",
        sha256="9202eff8d02a35542e368a790d0c3bc81530f618f28f8f57929e29df52bf7634",
    )
    version(
        "1.9.3",
        sha256="60addba214b3d2ad65a3aacdcfc7d02fe697da0f3aefb0f6229370f08280ed3d",
    )
    version(
        "1.9.2",
        sha256="39a0cce64af74b915c128dcad5f4c91c634b1d35d646405aff0b72c6491f6161",
    )
    version(
        "1.9.1",
        sha256="62fd4265c57918a8b9891a033fd5f10f868dc52a068233e0325f7892cf1c1fd0",
    )
    version(
        "1.9", sha256="7bd80f3daaf33ba73eb9579ec4fbaf841388e4e1357e5eafc227cfdd905b81a6"
    )

    patch("glut-link.patch", when="@:1.9.3")

    depends_on("freeglut")
    depends_on("ilcutil")

    def cmake_args(self):
        # install error if build_testing is off
        # see https://github.com/iLCSoft/CED/issues/7
        args = [self.define("BUILD_TESTING", True)]
        return args
