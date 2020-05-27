# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lccd(CMakePackage):
    """ Linear Collider Conditions Data toolkit."""

    homepage = "https://github.com/iLCSoft/lccd"
    git      = "https://github.com/iLCSoft/lccd.git"
    url      = "https://github.com/iLCSoft/lccd/archive/v01-05.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.5.0', sha256='876f751bebab760303b8dc3b7c6d4fe7d47ddd5aa19af9338f6565c5b817229b')

    variant('conddbmysql', default=True,
            description="builds with database support")


    depends_on("ilcutil")
    depends_on("conddbmysql", when="+conddbmysql")


    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define_from_variant('LCCD_CONDDBMYSQL', 'conddbmysql'))
        return args

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/iLCSoft/lccd/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/iLCSoft/lccd/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

