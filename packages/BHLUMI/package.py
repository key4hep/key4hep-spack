# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Bhlumi(AutotoolsPackage):

    """BHLUMI is the state of art Monte Carlo for e+e- -> e+e- gamma (gamma ...)."""

    homepage = "https://github.com/KrakowHEPSoft/BHLUMI"
    url      = "https://github.com/KrakowHEPSoft/BHLUMI/archive/4.04-linuxLHE.tar.gz"
    git      = "https://github.com/KrakowHEPSoft/BHLUMI.git"

    tags = ['hep']

    version('4.04-linuxLHE', sha256='266042ce18166807c45d4d9f6e543f8571a8479cf87f0da6b87312ed3129ef0f')

#     depends_on('autoconf', type='build')
#     depends_on('automake', type='build')
#     depends_on('libtool',  type='build')
#     depends_on('m4',       type='build')
#     depends_on('root')

    patch('BHLUMI-4.04-linuxLHE.patch', level=0)

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

#    @run_before('autoreconf')
#    def create_symlink(self):
#        os.symlink('dizet-6.45', 'dizet')
#
#
#    def autoreconf(self, spec, prefix):
#        autoreconf('--install', '--force')
#
#    def flag_handler(self, name, flags):
#        if name == 'cflags':
#            flags.append('-O2')
#            flags.append('-g0')
#        elif name == 'cxxflags':
#            flags.append('-O2')
#            flags.append('-g0')
#        elif name == 'fflags':
#            if self.spec.satisfies('%gcc@10:'):
#                if flags is None:
#                    flags = []
#                flags.append('-fallow-argument-mismatch')
#        return (flags, None, flags)

    def build(self, spec, prefix):
        with working_dir('4.x-cpc'):
            make('-f', 'makefile', 'lhemain')

    def install(self, spec, prefix):
        chmod = which('chmod')

        mkdirp(prefix.bin)

        install(join_path('4.x-cpc', 'demo2.exe'), join_path(prefix.bin, 'BHLUMI.exe'))
        chmod('755', join_path(prefix.bin, 'BHLUMI.exe'))

        script_sh = join_path(os.path.dirname(__file__), 'BHLUMI')
        script = script = prefix.bin.BHLUMI
        install(script_sh, script)
        chmod('755', script)

        mkdirp(prefix.etc.BHLUMI)

#         install('.KK2f_defaults', join_path(prefix.etc.KKMCee, 'KK2f_defaults'))
# 
#         mkdirp(prefix.etc.KKMCee.dizet)
#         for fn in ('mu', 'tau', 'nue', 'numu', 'nutau', 'up', 'down', 'botom'):
#             install(join_path('dizet', 'table.' + fn), prefix.etc.KKMCee.dizet)
# 
#         mkdirp(prefix.share.KKMCee.examples)
#         for fn in ('Mu', 'Tau', 'Up', 'Down', 'Botom', 'Beast', 'Inclusive'):
#             fo = 'Bottom' if fn == 'Botom' else fn
#             install(join_path('ffbench', fn, fn + '.input'), 
#                     join_path(prefix.share.KKMCee.examples, fo + '.input'))

        mkdirp(prefix.share.BHLUMI.iniseed)
        install_tree(join_path('4.x-cpc', 'iniseed'), prefix.share.BHLUMI.iniseed)

        mkdirp(prefix.share.BHLUMI.utils)
        install(join_path('4.x-cpc', 'semaphore.start'), prefix.share.BHLUMI.utils)
        install(join_path('4.x-cpc', 'semaphore.stop'), prefix.share.BHLUMI.utils)
