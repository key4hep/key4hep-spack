# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Aidatt(CMakePackage):
    """Tracking toolkit developed in the AIDA project."""

    homepage = "https://github.com/AIDASoft/aidaTT"
    url      = "https://github.com/AIDASoft/aidaTT/archive/v00-10.tar.gz"
    git      = "https://github.com/AIDASoft/aidaTT.git"

    maintainers = ['vvolkl']

    version("master", branch="master")
    version('0.10',     sha256='5379a369ee29bebeece7e814c0595bac9f08f2737ce03ae529b4b4e84dea1283')

    depends_on('ilcutil')
    depends_on('eigen')
    depends_on('generalbrokenlines')
    depends_on('dd4hep')
    depends_on('lcio')

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        if (len(version) == 2):
            url = base_url + "/v%s-%s.tar.gz" % (major, minor)
        elif (len(version) == 3):
            patch = (str(version[2]).zfill(2))
            if version[2] == 0:
                url = base_url + "/v%s-%s.tar.gz" % (major, minor)
            else:
                url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        else:
            print('Error - Wrong version format provided')
            return
        return url
