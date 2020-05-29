# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ilcutil(CMakePackage):
    """ A utility package for the iLCSoft software framework """

    homepage = "https://github.com/iLCSoft/ilcutil"
    git      = "https://github.com/iLCSoft/ilcutil.git"
    url      = "https://github.com/iLCSoft/ilcutil/archive/v01-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.6.0', sha256='09083890721704f39a3e902dc660db5326027cc38446b813233d04ec3233ba2e')

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/iLCSoft/ilcutil/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/iLCSoft/ilcutil/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

