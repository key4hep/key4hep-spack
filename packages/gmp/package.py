# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version

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
       return ilc_url_for_version(self, version)
