# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Marlinreco(CMakePackage):
    """Assembly of various Marlin processor for reconstruction."""

    url      = "https://github.com/iLCSoft/MarlinReco/archive/v01-27.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinReco"
    git      = "https://github.com/iLCSoft/MarlinReco.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.27', sha256='097462b714e9a47c90154ae1a82de44946d6473b07a659c810263ae53dc8253c')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlinkinfit')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('root')
    depends_on('boost')
    depends_on('dd4hep')
    depends_on('raida')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinReco.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
