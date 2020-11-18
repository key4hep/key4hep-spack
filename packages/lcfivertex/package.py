# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version


class Lcfivertex(CMakePackage, Ilcsoftpackage):
    """Package for vertex finding as well as vertex charge determination in b- and c-jets."""

    url      = "https://github.com/iLCSoft/LCFIVertex/archive/v00-08.tar.gz"
    homepage = "https://github.com/iLCSoft/LCFIVertex"
    git      = "https://github.com/iLCSoft/LCFIVertex.git"

    maintainers = ['vvolkl']
    
    version('master',  branch='master')
    k4_add_latest_commit_as_version(git)
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
