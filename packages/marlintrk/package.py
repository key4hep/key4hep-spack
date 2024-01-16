# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlintrk(CMakePackage, Ilcsoftpackage):
    """Tracking Package based on LCIO and GEAR,
    primarily aimed at providing track fitting in Marlin."""

    homepage = "https://github.com/iLCSoft/MarlinTrk"
    url = "https://github.com/iLCSoft/MarlinTrk/archive/v02-08.tar.gz"
    git = "https://github.com/iLCSoft/MarlinTrk.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "2.9.1",
        sha256="3a4d8f3208423cae414e40cd359d73d366445d30ccb24574574bd29443c914f2",
    )
    version(
        "2.9", sha256="a1ccec25aea02d62f22d98cffc870ac199e455aa31100b6fa8795a8dc34cdcc0"
    )
    version(
        "2.8", sha256="bd3b0074c06e2b778c74d1aeb2c989c39100a8adf5018792db599f84cb946c14"
    )
    version(
        "2.7", sha256="c6e556d18ae6f2f3ae6c0fd8aa4322ce866e08b54b48ce95d09636443eff53ea"
    )

    variant("gear", default=False, description="Provide Gear backward compatibility")

    depends_on("ilcutil")
    depends_on("lcio")
    depends_on("gear", when="+gear")
    depends_on("kaltest")
    depends_on("kaldet")
    depends_on("root")
    depends_on("ddkaltest")
    depends_on("clhep")
    depends_on("aidatt")
    depends_on("gsl")
    depends_on("generalbrokenlines")

    def cmake_args(self):
        args = [
            self.define_from_variant("MARLINTRK_USE_GEAR", "gear"),
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
        ]
        return args
