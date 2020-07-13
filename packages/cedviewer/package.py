# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Cedviewer(CMakePackage):
    """CEDViewer processor for the CED event display."""

    url      = "https://github.com/iLCSoft/CEDViewer/archive/v01-17-01.tar.gz"
    homepage = "https://github.com/iLCSoft/CEDViewer"
    git      = "https://github.com/iLCSoft/CEDViewer.git"

    maintainers = ['vvolkl']

    version('1.17.1', sha256='e778396dc6d9c106888c30bc11695a2283be68a5ced155df72cd5ec7d3c3f648')

    depends_on('ced')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('ilcutil')
    depends_on('dd4hep')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_LDD', self.prefix.lib + "/libCEDViewer.so")


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
