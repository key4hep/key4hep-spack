# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Marlinreco(CMakePackage, Ilcsoftpackage):
    """Assembly of various Marlin processor for reconstruction."""

    url      = "https://github.com/iLCSoft/MarlinReco/archive/v01-27.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinReco"
    git      = "https://github.com/iLCSoft/MarlinReco.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.32', sha256='0ea3bee03e2bec1924b5876675043b592a942bc8cf306eb7056eaf03ac1748f6')
    version('1.31', sha256='eeb823f2476e1d31a54997b1a09fcc20cc8f3555a9f677054eacd5f44d4f59ee')
    version('1.30', sha256='e3b22a3f974232e4cc785326ad0dfd283b377cffda3245166f419b170276b6ff')
    version('1.29', sha256='45a36bb98f26580c182848d73ef0423290f99eae380f0cb27eea48f4ef48e459')
    version('1.28', sha256='f0a6a081d9816502950e639bc209f8f264e63ff3ba555640eff3fb61fb4bdd1d')
    version('1.27', sha256='097462b714e9a47c90154ae1a82de44946d6473b07a659c810263ae53dc8253c')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlinkinfit')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('root')
    depends_on('boost')
    depends_on('dd4hep')
    depends_on('raida')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinReco.so")

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
