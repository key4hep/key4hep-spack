# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Garlic(CMakePackage, Ilcsoftpackage):
    """Garlic is a Marlin Processor to identify photons and electrons."""

    url      = "https://github.com/iLCSoft/Garlic/archive/v03-01.tar.gz"
    homepage = "https://github.com/iLCSoft/Garlic"
    git      = "https://github.com/iLCSoft/Garlic.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('3.1', sha256='a35bea352d0c6aaa7d289656f6272be216e9b8ada2a750461ceed7c2cf780940')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libGarlic.so")
