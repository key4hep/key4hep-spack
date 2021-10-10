# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage

class Cedviewer(CMakePackage, Ilcsoftpackage):
    """CEDViewer processor for the CED event display."""

    url      = "https://github.com/iLCSoft/CEDViewer/archive/v01-17-01.tar.gz"
    homepage = "https://github.com/iLCSoft/CEDViewer"
    git      = "https://github.com/iLCSoft/CEDViewer.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.18', sha256='46d188d102cbb414b4534e357e506c370644f2df8eada5565a2bcf234a282141')
    version('1.17.1', sha256='e778396dc6d9c106888c30bc11695a2283be68a5ced155df72cd5ec7d3c3f648')

    depends_on('ced')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('ilcutil')
    depends_on('dd4hep')
    depends_on('root')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libCEDViewer.so")

    def cmake_args(self):
        return [
            '-DCMAKE_CXX_STANDARD=%s'
            % self.spec['root'].variants['cxxstd'].value
        ]
