# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Gmp(CMakePackage):
    """GMP Wrapper"""

    homepage = "https://github.com/key4hep/GMP"
    git      = "https://github.com/key4hep/GMP.git"
    url      = "https://github.com/key4hep/GMP/archive/v00-01.tar.gz"

    maintainers = ['fdplacido']

    version('master', branch='master')
    version('0.1', sha256='649ffa462e75c716f54b4e0b530c27c27a7f62a8fad64af8aecc646046045efd')

    depends_on('root')
    depends_on('lcio')
    depends_on('marlin')
    depends_on('gaudi')

    def cmake_args(self):
        args = [
            self.define('HOST_BINARY_TAG','x86_64-linux-gcc9-opt')
        ]
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        if (len(version) == 2):
            url = "https://github.com/key4hep/GMP/archive/v%s-%s.tar.gz" % (major, minor)
        elif (len(version) == 3):
            patch = (str(version[2]).zfill(2))
            url = "https://github.com/key4hep/GMP/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        else:
            print('Error - Wrong version format provided')
            return
        return url
