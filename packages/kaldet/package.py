# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Kaldet(CMakePackage, Ilcsoftpackage):
    """Kaldet: part of ilcsoft tracking."""

    homepage = "https://github.com/iLCSoft/KalDet"
    url      = "https://github.com/iLCSoft/KalDet/archive/v01-14-01.tar.gz"
    git      = "https://github.com/iLCSoft/KalDet.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.14.1',  sha256='39386f8d9648ebfd9771d99f2d318c5214a5560ad4135a12b90b0f3662681e6d')
    version('1.14',     sha256='67eb70874f9cd1d85d0a192e40e3e2ec3ecd03b6e2746bb2e1bdcf1b40c9c32a')
    version('1.13',     sha256='3d299dae6622560881365acc5e9b572faefc39dbeee453562d0d9b9ab2795633')
    version('1.12',     sha256='d7f0dbcea955de607a2b844de749e2e9a0cfd3bd9aef6dde871398eb2b7656cc')
    version('1.11',     sha256='8028d0e94d8bbdc7047f1897847c9bdf4fd7d2ba9d0120413100569a9922d753')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('gear')
    depends_on('kaltest')
    depends_on('root')

    patch("dict.patch")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def setup_run_environment(self, env):
        env.prepend_path('CPATH', self.prefix.include.kaldet)
