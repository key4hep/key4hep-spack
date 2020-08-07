# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Ddmarlinpandora(CMakePackage):
    """Interface between Marlin and PandoraPFA."""

    url      = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.11', sha256='92410186209508091e0a8e330986283ffb32e40fd7195d10aad1a6a2e953f3ee')

    depends_on('ilcutil')
    depends_on('marlinutil')
    depends_on('marlin')
    depends_on('pandorapfa')
    depends_on('dd4hep')
    depends_on('marlintrk')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinDD4hep.so")


    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
