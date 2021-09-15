# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Marlintrkprocessors(CMakePackage, Ilcsoftpackage):
    """A collection of Tracking Relelated Processors Based on MarlinTrk"""

    url      = "https://github.com/iLCSoft/MarlinTrkProcessors/archive/v02-11.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinTrkProcessors"
    git      = "https://github.com/iLCSoft/MarlinTrkProcessors.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('2.11', sha256='49a567831e2b7a0c43ded955ce31fbe7d467a59960f4bcc2c2120e20762639b0')

    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('ddkaltest')
    depends_on('raida')


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinTrkProcessors.so")
