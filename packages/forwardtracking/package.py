# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Forwardtracking(CMakePackage, Ilcsoftpackage):
    """Track Reconstruction for the Forward Direction (for the FTD)"""

    url      = "https://github.com/iLCSoft/ForwardTracking/archive/v01-14.tar.gz"
    homepage = "https://github.com/iLCSoft/ForwardTracking"
    git      = "https://github.com/iLCSoft/ForwardTracking.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.14', sha256='99149d170a1ae179500b2c47ec79dca227ff96c0bdf0cd69f2075eb468177a5e')

    patch('testing.patch', when="@:1.15")


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('root')
    depends_on('clhep')
    depends_on('raida')

    def cmake_args(self):
        args = []
        args.append(self.define('BUILD_TESTING', self.run_tests))
        args.append(self.define('CMAKE_CXX_STANDARD',
                                self.spec['root'].variants['cxxstd'].value))
        return args


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libForwardTracking.so")
