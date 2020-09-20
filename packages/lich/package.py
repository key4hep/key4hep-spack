# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Lich(CMakePackage):
    """A marlin processor applied on PFOs for charged particle PID."""

    url      = "https://github.com/danerdaner/LICH/archive/v00-01.tar.gz"
    homepage = "https://github.com/danerdaner/LICH"
    git      = "https://github.com/danerdaner/LICH.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.1', sha256='9c5358f76c64b9f28734b82cca31101e09faa67b6ffd340889488c761aea918c')

    depends_on('ilcutil')
    depends_on('marlinutil')
    depends_on('marlin')
    depends_on('root')
    
    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libLICH.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
