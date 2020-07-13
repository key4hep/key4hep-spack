# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Kitrackmarlin(CMakePackage):
    """Implementation of classes for the use of KiTrack by Marlin"""

    url      = "https://github.com/iLCSoft/KiTrackMarlin/archive/v01-13.tar.gz"
    homepage = "https://github.com/iLCSoft/KiTrackMarlin"
    git      = "https://github.com/iLCSoft/KiTrackMarlin.git"

    maintainers = ['vvolkl']

    version('1.13', sha256='1307578313673fae159aa6fb4eacf3f22bfa085c61337d14a5895e078a8d7f70')

    depends_on('kitrack')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('dd4hep')
    depends_on('clhep')

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
