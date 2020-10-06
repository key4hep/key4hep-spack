# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Marlinfastjet(CMakePackage):
    """Marlin processor to interface FastJet."""

    url      = "https://github.com/iLCSoft/MarlinFastjet/archive/v00-05-02.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinFastjet"
    git      = "https://github.com/iLCSoft/MarlinFastjet.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.5.2', sha256='abdffa6c2c9328bb094456f6003920d0c860e7faa5c76aea650da9e47e698bdf')


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('fastjet')
    depends_on('fjcontrib')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinFastJet.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
