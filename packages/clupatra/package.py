# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Clupatra(CMakePackage):
    """Topological pattern recognition (for the TPC)"""

    url      = "https://github.com/iLCSoft/Clupatra/archive/v01-03.tar.gz"
    homepage = "https://github.com/iLCSoft/Clupatra"
    git      = "https://github.com/iLCSoft/Clupatra.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.3', sha256='5256d1b120157e9a6916f86249e589d0ea386c4e6dac83fec0294b753a779c25')

    depends_on('ilcutil')
    depends_on('gsl')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('root')
    depends_on('marlintrk')
    depends_on('kaltest')


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libClupatra.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
