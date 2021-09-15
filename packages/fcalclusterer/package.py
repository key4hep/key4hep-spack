# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Fcalclusterer(CMakePackage, Ilcsoftpackage):
    """Reconstruction for the Forward Calorimeters of Future e+e- colliders."""

    url      = "https://github.com/FCalSW/FCalClusterer/archive/v01-00-01.tar.gz"
    homepage = "https://github.com/FCalSW/FCalClusterer"
    git      = "https://github.com/FCalSW/FCalClusterer.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.0.3', sha256='5360ccb85f8742d9f4b84c7a3bb3ed3574b534f1b08240100c5b4e48e8ffa35e')
    version('1.0.2', sha256='6c6898f8641743a7654b1c1e7b3a52643be9d23f8bb3624e415c51549ac64cbe')
    version('1.0.1', sha256='87837d7fd802e46c8530c721035ae75946d699031f093612ec02a7fabe0c6143')

    depends_on('ilcutil')
    depends_on('lcio')
    depends_on('gear')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('root +unuran +math')
    depends_on('dd4hep')

    # CMAKE_INSTALL_PREFIX is overwritten by the package
    patch("install.patch", when="@:1.0.1")
    patch("random-shuffle-c17.patch", when="@:1.0.1")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    @run_after('install')
    def install_source(self):
        #make('install')
        install_tree('.', self.prefix)

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libFCalClusterer.so")
