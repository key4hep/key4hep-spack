# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Kaldet(CMakePackage):
    """Kaldet: part of ilcsoft tracking."""

    homepage = "https://github.com/iLCSoft/KalDet"
    url      = "https://github.com/iLCSoft/KalDet/archive/v01-14-01.tar.gz"
    git      = "https://github.com/iLCSoft/KalDet.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('01-14-01',  sha256='39386f8d9648ebfd9771d99f2d318c5214a5560ad4135a12b90b0f3662681e6d')
    version('01-14',     sha256='67eb70874f9cd1d85d0a192e40e3e2ec3ecd03b6e2746bb2e1bdcf1b40c9c32a')
    version('01-13',     sha256='3d299dae6622560881365acc5e9b572faefc39dbeee453562d0d9b9ab2795633')
    version('01-12',     sha256='d7f0dbcea955de607a2b844de749e2e9a0cfd3bd9aef6dde871398eb2b7656cc')
    version('01-11',     sha256='8028d0e94d8bbdc7047f1897847c9bdf4fd7d2ba9d0120413100569a9922d753')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('gear')
    depends_on('kaltest')
    depends_on('root')
    depends_on('ilcsoft')
