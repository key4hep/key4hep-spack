# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fccconfig(CMakePackage):
    """"""

    homepage = "https://github.com/HEP-FCC/FCC-config"
    git = "https://github.com/HEP-FCC/FCC-config"

    maintainers = ["jmcarcell"]

    version("main", branch="main")

    def cmake_args(self):
        args = []
        args.append("-DBUILD_TESTING=%s" % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.prepend_path("FCCCONFIG", self.prefix)
