# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FccConfig(CMakePackage):
    """"""

    homepage = "https://github.com/HEP-FCC/FCC-config"
    url = "https://github.com/HEP-FCC/FCC-config/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/HEP-FCC/FCC-config"

    maintainers = ["jmcarcell"]

    version("main", branch="main")
    version(
        "0.1.0",
        sha256="f609d88a1a6fbbdad50b8988012d80b8dad5c5fe31d6788761a7b06e1561736c",
    )

    def cmake_args(self):
        args = []
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.set("FCCCONFIG", self.prefix)
