# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Kkmcee(AutotoolsPackage):

    """KKMCee is the state of art Monte Carlo for e+e- -> ffbar."""

    homepage = "https://github.com/KrakowHEPSoft/KKMCee"
    url      = "https://github.com/KrakowHEPSoft/KKMCee/archive/V4.30.tar.gz"
    git      = "https://github.com/KrakowHEPSoft/KKMCee.git"

    tags = ['hep']

    version('4.30', sha256='5c650eb464a6d673858a2d4421084d90ccc30c90f35d9e46f18fc1167d5a5bdf')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('root')

    patch('KKMCee-dev-4.30.patch', level=0)
    patch('gcc4.patch')
    patch('gcc6.patch')
    patch('gcc5.patch')

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    @run_before('autoreconf')
    def create_symlink(self):
        os.symlink('dizet-6.45', 'dizet')


    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--force')

    def configure_args(self):
        args = []
        args += ["CXX=c++"]
        args += ["CC=cc"]
        return args


    def flag_handler(self, name, flags):
        if name == 'cflags':
            flags.append('-O2')
            flags.append('-g0')
        elif name == 'cxxflags':
            flags.append('-O2')
            flags.append('-g0')
        elif name == 'fflags':
            if self.spec.satisfies('%gcc@10:') or self.spec.satisfies('%clang@11:') or self.spec.satisfies('%apple-clang@11:'):
                if flags is None:
                    flags = []
                #flags.append('-fallow-argument-mismatch')
                flags.append('-Wno-argument-mismatch')
        return (flags, None, flags)

    def build(self, spec, prefix):
        with working_dir('ffbench'):
            make('-f', 'KKMakefile', 'makflag')
            make('-f', 'KKMakefile', 'makprod')
            make('-f', 'KKMakefile', 'EWtables')
            make('-f', 'KKMakefile', 'ProdMC.exe')

    def install(self, spec, prefix):
        chmod = which('chmod')

        mkdirp(prefix.bin)

        install(join_path('ffbench', 'ProdMC.exe'), join_path(prefix.bin, 'KKMCee.exe'))
        chmod('755', join_path(prefix.bin, 'KKMCee.exe'))

        script_sh = join_path(os.path.dirname(__file__), 'KKMCee')
        script = script = prefix.bin.KKMCee
        install(script_sh, script)
        chmod('755', script)

        mkdirp(prefix.etc.KKMCee)

        install('.KK2f_defaults', join_path(prefix.etc.KKMCee, 'KK2f_defaults'))

        mkdirp(prefix.etc.KKMCee.dizet)
        for fn in ('mu', 'tau', 'nue', 'numu', 'nutau', 'up', 'down', 'botom'):
            install(join_path('dizet', 'table.' + fn), prefix.etc.KKMCee.dizet)

        mkdirp(prefix.share.KKMCee.examples)
        for fn in ('Mu', 'Tau', 'Up', 'Down', 'Botom', 'Beast', 'Inclusive'):
            fo = 'Bottom' if fn == 'Botom' else fn
            install(join_path('ffbench', fn, fn + '.input'), 
                    join_path(prefix.share.KKMCee.examples, fo + '.input'))

        mkdirp(prefix.share.KKMCee.iniseed)
        install_tree(join_path('ffbench', 'iniseed'), prefix.share.KKMCee.iniseed)

        mkdirp(prefix.share.KKMCee.utils)
        install(join_path('ffbench', 'semaphore.start'), prefix.share.KKMCee.utils)
        install(join_path('ffbench', 'semaphore.stop'), prefix.share.KKMCee.utils)
