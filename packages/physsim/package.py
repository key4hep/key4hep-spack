# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Physsim(CMakePackage):
    """Physsim is a matrix element package."""

    url      = "https://github.com/iLCSoft/Physsim/archive/v00-04-01.tar.gz"
    homepage = "https://github.com/iLCSoft/Physsim"
    git      = "https://github.com/iLCSoft/Physsim.git"

    maintainers = ['vvolkl']

    version('0.4.1', sha256='4c22eee5dcccb764a5ff90850aeb33563c45a14af8939a3ebea736c7d92ac1c1')

    depends_on('ilcutil')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libPhysSim.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
