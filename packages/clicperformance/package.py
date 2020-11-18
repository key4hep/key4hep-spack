# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version


class Clicperformance(CMakePackage, Ilcsoftpackage):
    """ Package containing processors and configurations to determine the performance of the CLIC detector model"""

    url      = "https://github.com/iLCSoft/ClicPerformance/archive/v02-04.tar.gz"
    homepage = "https://github.com/iLCSoft/ClicPerformance"
    git      = "https://github.com/iLCSoft/ClicPerformance.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('root')
    depends_on('dd4hep')
    depends_on('raida')


    #TODO: build_testing

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libClicPerformance.so")
