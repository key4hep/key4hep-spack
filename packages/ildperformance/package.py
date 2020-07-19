# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Ildperformance(CMakePackage):
    """Assembly of various Marlin processor for reconstruction."""

    url      = "https://github.com/iLCSoft/ILDPerformance/archive/v01-08.tar.gz"
    homepage = "https://github.com/iLCSoft/ILDPerformance"
    git      = "https://github.com/iLCSoft/ILDPerformance.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.8', sha256='bcf19d3a6f425fa5eea228676d07558635881a0329c4d66ffda4230dfe9617c1')


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('generalbrokenlines')
    depends_on('aidatt')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('root')
    depends_on('dd4hep')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libILDPerformance.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
