# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Physsim(CMakePackage):
    """Physsim is a matrix element package."""

    url      = "https://github.com/iLCSoft/Physsim/archive/v00-04-01.tar.gz"
    homepage = "https://github.com/iLCSoft/Physsim"
    git      = "https://github.com/iLCSoft/Physsim.git"

    maintainers = ['vvolkl']

    tags = ['hep']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.4.1', sha256='4c22eee5dcccb764a5ff90850aeb33563c45a14af8939a3ebea736c7d92ac1c1')

    depends_on('ilcutil')
    depends_on('root')

    patch("dict.patch")

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libPhyssim.so")

    def setup_run_environment(self, spack_env):
        # The dictionary headers require physsim to be in CPATH or ROOT_INCLUDE_PATH
        spack_env.prepend_path('CPATH', self.prefix.include.physsim)

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
