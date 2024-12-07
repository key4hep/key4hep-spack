# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4pandora(CMakePackage, Key4hepPackage):
    """k4Pandora is a pandora app for the Key4HEP software framework"""

    homepage = "https://github.com/key4hep/k4Pandora"
    url = "https://github.com/key4hep/k4Pandora/archive/master.tar.gz"
    git = "https://github.com/key4hep/k4Pandora.git"

    tags = ["hep", "key4hep"]

    maintainers = ["mirguest"]

    version("master", branch="master")

    depends_on("clhep")
    depends_on("dd4hep")
    depends_on("edm4hep")
    depends_on("k4fwcore@0.3.0:")
    depends_on("gaudi@35.0:")
    depends_on("gear")
    depends_on("lcio")
    depends_on("lccontent")
    depends_on("hepmc")
    depends_on("pandorasdk")
    depends_on("pandorapfa")
    depends_on("root")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}"
        )

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append("-DCMAKE_MODULE_PATH=%s" % cmake_modules)
        return args
