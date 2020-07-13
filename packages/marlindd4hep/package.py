# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Marlindd4hep(CMakePackage):
    """Provides one processor to initialize a DD4hep detector geometry from a compact file for a Marlin job."""

    url      = "https://github.com/iLCSoft/MarlinDD4hep/archive/v00-06.tar.gz"

    maintainers = ['vvolkl']

    version('0.6', sha256='1cf8eb03bbdf6da8fbf277d8168d97f77e1675850a7e66d0e9f90684e3a2f077')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('dd4hep')

    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define('INSTALL_DOC', False))
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_LDD', self.prefix.lib + "/libMarlinDD4hep.so.so")


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
