# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Kitrackmarlin(CMakePackage, Ilcsoftpackage):
    """Implementation of classes for the use of KiTrack by Marlin"""

    url      = "https://github.com/iLCSoft/KiTrackMarlin/archive/v01-13.tar.gz"
    homepage = "https://github.com/iLCSoft/KiTrackMarlin"
    git      = "https://github.com/iLCSoft/KiTrackMarlin.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.13.1', sha256='3dabd7a0a9ba9aba7c5ef17809dbe6a6e55b1200b33cf12567d0e3e3e91dd15f')
    version('1.13', sha256='1307578313673fae159aa6fb4eacf3f22bfa085c61337d14a5895e078a8d7f70')

    depends_on('kitrack')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('gsl')
    depends_on('dd4hep')
    depends_on('clhep')

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
