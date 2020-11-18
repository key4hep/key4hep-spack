# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version


class Lctuple(CMakePackage, Ilcsoftpackage):
    """Marlin package that creates a ROOT TTree with a column wise ntuple from LCIO collections."""

    url      = "https://github.com/iLCSoft/LCTuple/archive/v01-12.tar.gz"
    homepage = "https://github.com/iLCSoft/LCTuple"
    git      = "https://github.com/iLCSoft/LCTuple.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.12', sha256='e0e7c4c86f257027a7e9b1c42438087a7b0919964f9719080be25df8a0f95968')


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libLCTuple.so")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args
