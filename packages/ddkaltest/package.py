# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Ddkaltest(CMakePackage, Ilcsoftpackage):
    """Interface between KalTest fitter and DD4hep based geometry"""

    homepage = "https://github.com/iLCSoft/DDKalTest"
    url = "https://github.com/iLCSoft/DDKalTest/archive/v01-06.tar.gz"
    git = "https://github.com/iLCSoft/DDKalTest.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.7", sha256="5126404bcad2f6f669ef8f02c80de097196e346f5945e7f6249820f8cd5fd86c"
    )
    version(
        "1.6", sha256="e668242d84eb94e59edca18e524b1a928fcf7ae7c4b79f76f0338a0a4e835d8f"
    )
    version(
        "1.5", sha256="4ef6fea7527dbb5f9a12322e92e27d80f2c29b115aae13987f55cb6cf02f31f5"
    )

    depends_on("dd4hep")
    depends_on("root")
    depends_on("ilcutil")
    depends_on("lcio")
    depends_on("gsl")
    depends_on("kaltest")
    depends_on("aidatt")

    @run_after("install")
    def installheaders(self):
        # make('install')
        install_tree(".", self.prefix)

    def cmake_args(self):
        # C++ Standard
        return [f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"]
