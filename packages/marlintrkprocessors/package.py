# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Marlintrkprocessors(CMakePackage):
    """A collection of Tracking Relelated Processors Based on MarlinTrk"""

    url      = "https://github.com/iLCSoft/MarlinTrkProcessors/archive/v02-11.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinTrkProcessors"
    git      = "https://github.com/iLCSoft/MarlinTrkProcessors.git"

    maintainers = ['vvolkl']

    version('2.11', sha256='49a567831e2b7a0c43ded955ce31fbe7d467a59960f4bcc2c2120e20762639b0')

    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('ddkaltest')
    depends_on('raida')


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_LDD', self.prefix.lib + "/libMarlinTrkProcessors.so")

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

