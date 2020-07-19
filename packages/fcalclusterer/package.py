# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Fcalclusterer(CMakePackage):
    """Reconstruction for the Forward Calorimeters of Future e+e- colliders."""

    url      = "https://github.com/FCalSW/FCalClusterer/archive/v01-00-01.tar.gz"
    homepage = "https://github.com/FCalSW/FCalClusterer"
    git      = "https://github.com/FCalSW/FCalClusterer.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.0.1', sha256='87837d7fd802e46c8530c721035ae75946d699031f093612ec02a7fabe0c6143')

    depends_on('ilcutil')
    depends_on('lcio')
    depends_on('gear')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('root')
    depends_on('dd4hep')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libFCalClusterer.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
