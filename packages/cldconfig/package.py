# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cldconfig(CMakePackage):
    """Configuration files for the CLD detector concept"""

    homepage = "https://github.com/key4hep/CLDConfig"
    git = "https://github.com/key4hep/CLDConfig"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    depends_on("k4geo", type="test")
    depends_on("dd4hep", type="test")
    depends_on("k4fwcore", type="test")

    def cmake_args(self):
        args = []
        if "root" in self.spec:
            args.append(
                f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
            )
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args
