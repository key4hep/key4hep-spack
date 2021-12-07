# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os


class Babayaga(MakefilePackage):

    """Babayaga is the state of art Monte Carlo for e+e- -> gamma gamma"""

    homepage = "http://neowulf.pv.infn.it:8281/babayaga-fcc/"
    url      = "http://neowulf.pv.infn.it:8281/babayaga-fcc/babayaga-fcc.tar.bz2"

    tags = ['hep']

    version('fcc-1.0.0', sha256='bfd474e267972ae06d7e622de87db7ba5edcbb2e1323838d4a299ac3cd23dce8')

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    # babayaga bundles recola version 1.4 and needs cmake for that
    depends_on('cmake', type=('build'))

    patch('makefile_compiler1.patch')

    # there seems to be a race condition that leads to build failures
    parallel = False

    def build(self, spec, prefix):
        with working_dir('.'):
            make('-f', 'Makefile', 'babayaga-fcc')

    def install(self, spec, prefix):
        chmod = which('chmod')

        mkdirp(prefix.bin)

        install('babayaga-fcc', join_path(prefix.bin, 'babayaga-fcc.exe'))
        chmod('755', join_path(prefix.bin, 'babayaga-fcc.exe'))

        script_sh = join_path(os.path.dirname(__file__), 'babayaga')
        script = script = prefix.bin.babayaga
        install(script_sh, script)
        chmod('755', script)

