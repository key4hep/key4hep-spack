# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Gmp(CMakePackage):
    """GMP Wrapper"""

    homepage = "https://github.com/key4hep/GMP"
    git      = "https://github.com/key4hep/GMP.git"
    url      = "https://github.com/key4hep/GMP/archive/master.tar.gz"

    maintainers = ['fdplacido']

    version('develop', branch='master')

    depends_on('root')
    depends_on('lcio')
    depends_on('marlin')
    depends_on('gaudi')

    def cmake_args(self):
        args = [
            self.define('HOST_BINARY_TAG','x86_64-linux-gcc9-opt')
        ]
        return args
