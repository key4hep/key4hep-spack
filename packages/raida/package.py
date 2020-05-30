# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Raida(CMakePackage):
    """ A utility package for the iLCSoft software framework """

    homepage = "https://github.com/iLCSoft/raida"
    git      = "https://github.com/iLCSoft/raida.git"
    url      = "https://github.com/iLCSoft/raida/archive/v01-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.9.0', sha256='53ad3fd7c62e5eba70e6d6099e5ef4d92920399afb7b31dc8008b6ad865a9e85')


    depends_on('ilcutil')
    depends_on("root")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/iLCSoft/raida/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/iLCSoft/raida/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

