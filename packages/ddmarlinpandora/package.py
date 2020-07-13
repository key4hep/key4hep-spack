# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ddmarlinpandora(CMakePackage):
    """Interface between Marlin and PandoraPFA."""

    url      = "https://github.com/iLCSoft/DDMarlinPandora/archive/v00-11.tar.gz"

    maintainers = ['vvolkl']

    version('0.11', sha256='92410186209508091e0a8e330986283ffb32e40fd7195d10aad1a6a2e953f3ee')

    depends_on('ilcutil')
    depends_on('marlinutil')
    depends_on('marlin')
    depends_on('pandorasdk')
    depends_on('dd4hep')
    depends_on('marlintrk')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_LDD', self.prefix.lib + "/libMarlinDD4hep.so")


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
