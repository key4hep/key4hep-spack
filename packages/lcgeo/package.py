# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lcgeo(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/iLCSoft/lcgeo"
    git      = "https://github.com/iLCSoft/lcgeo"
    url      = "https://github.com/iLCSoft/lcgeo/archive/v00-16-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.16.6', sha256='0eef7137ad69b771e5cf8a3f4a71e060e9d57ee825d8d944fa6a0dec8c2dad60')
    version('0.16.5', sha256='a46738b2479c0469b06584f82801bf2dd546623180300753de0b5684abd12a05')

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('lcio')
    depends_on('dd4hep +geant4')
    depends_on('boost')
    depends_on('root')


    def cmake_args(self):
        args = []  
        args.append(self.define('CMAKE_CXX_STANDARD', self.spec.variants['cxxstd'].value))
        args.append(self.define('BUILD_TESTING', self.run_tests))
        return args

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/iLCSoft/lcgeo/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/iLCSoft/lcgeo/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
