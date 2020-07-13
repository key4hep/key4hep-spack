# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Pandorapfa(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    url      = "https://github.com/PandoraPFA/PandoraPFA/archive/v03-14-00.tar.gz"
    hompage  = "https://github.com/PandoraPFA/PandoraPFA"
    git      = "https://github.com/PandoraPFA/PandoraPFA.git"

    maintainers = ['vvolkl']

    version('3.14.0', sha256='1490f2504bdbd2960cba35fc552b762e3842d77ed5227f84ddabfde546fe6810')

    def cmake_args(self):
        args = ['-DLC_PANDORA_CONTENT=ON',
                '-DLAR_PANDORA_CONTENT=ON',
                "-DCMAKE_CXX_FLAGS=-std=c++17"]
        return args

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

