# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Forwardtracking(CMakePackage):
    """Track Reconstruction for the Forward Direction (for the FTD)"""

    url      = "https://github.com/iLCSoft/ForwardTracking/archive/v01-14.tar.gz"
    homepage = "https://github.com/iLCSoft/ForwardTracking"
    git      = "https://github.com/iLCSoft/ForwardTracking.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.14', sha256='99149d170a1ae179500b2c47ec79dca227ff96c0bdf0cd69f2075eb468177a5e')


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

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libForwardTracking.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
