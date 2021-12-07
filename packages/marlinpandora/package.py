# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlinpandora(CMakePackage, Ilcsoftpackage):
    """Pandora app for Marlin"""

    url      = "https://github.com/PandoraPFA/MarlinPandora/archive/v03-00-01.tar.gz"
    homepage = "https://github.com/PandoraPFA/MarlinPandora"
    git      = "https://github.com/PandoraPFA/MarlinPandora.git"


    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.0.1', sha256='2caecf5aa804dc0a0e2e4d6e87ad9100f76eafd1fd258f73130a9b476f9a4378')


    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('pandorapfa')
    depends_on('pandorasdk')
    depends_on('lccontent')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinPandora.so")

    def cmake_args(self):
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
