# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os


class Bhlumi(MakefilePackage):

    """BHLUMI is the state of art Monte Carlo for e+e- -> e+e- gamma (gamma ...)."""

    homepage = "https://github.com/KrakowHEPSoft/BHLUMI"
    url      = "https://github.com/KrakowHEPSoft/BHLUMI/archive/4.04-linuxLHE.tar.gz"
    git      = "https://github.com/KrakowHEPSoft/BHLUMI.git"

    tags = ['hep']

    version('4.04-linuxLHE', sha256='266042ce18166807c45d4d9f6e543f8571a8479cf87f0da6b87312ed3129ef0f')

    patch('BHLUMI-4.04-linuxLHE.patch', level=0)

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

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

