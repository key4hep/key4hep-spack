# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinutil(CMakePackage, Ilcsoftpackage):
    """Library that contains classes and functions that are used by more
    than one processor. In particular it contains the geometry classes that
    are used until we have the geometry for reconstruction package (GEAR)."""

    homepage = "https://github.com/iLCSoft/MarlinUtil/"
    url = "https://github.com/iLCSoft/MarlinUtil/archive/v01-15-01.tar.gz"
    git = "https://github.com/iLCSoft/MarlinUtil.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.17",
        sha256="0ac4f4b6b62cf5baeda4f585e205c0a77f55bafd7b968b1a664d5a7535ca3875",
    )
    version(
        "1.16.2",
        sha256="1dbed3ad127da340b816cda500515b267f26614ec21e9f70fa44ca52eb401803",
    )
    version(
        "1.16.1",
        sha256="f8e03cba4144b9797fa01321aeb1c2f01967d1fcb10089e7b1765c32e4346508",
    )
    version(
        "1.16",
        sha256="7f80a726e3b08653a88487b87618fca277d59fe22a448ce15043f8495f1108e9",
    )
    version(
        "1.15.1",
        sha256="05e878c9aae4a675e37ad2c63abc0b1c4c2a45dcb2e3c9ae5c31e7e6f64118bf",
    )

    depends_on("ilcutil")
    depends_on("marlin")
    depends_on("clhep")
    depends_on("gsl")
    depends_on("ced")
    depends_on("dd4hep")
    depends_on("root")

    def cmake_args(self):
        spec = self.spec
        cxxstd = spec["root"].variants["cxxstd"].value
        # Make sure that we pick the right GSL
        return [
            "-DCMAKE_CXX_STANDARD={0}".format(cxxstd),
            "-DGSL_DIR={}".format(self.spec["gsl"].prefix),
        ]
