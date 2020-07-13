# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lcfivertex(CMakePackage):
    """Package for vertex finding as well as vertex charge determination in b- and c-jets."""

    url      = "https://github.com/iLCSoft/LCFIVertex/archive/v00-08.tar.gz"
    homepage = "https://github.com/iLCSoft/LCFIVertex"
    git      = "https://github.com/iLCSoft/LCFIVertex.git"

    maintainers = ['vvolkl']
    
    version('master',  branch="master")
    version('0.8', sha256='37f3ea8754cefb60073471c298b4c1926ef9858e8edb4c51affa1ff7de4e2fb8')

    depends_on('lcio')
    depends_on('boost')
    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('raida')

    patch('tixml.patch', when="@0.8")

    def cmake_args(self):
        args = [self.define('INSTALL_DOC', False)]
        return args

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
