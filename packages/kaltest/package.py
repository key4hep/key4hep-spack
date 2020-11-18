# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version


class Kaltest(CMakePackage, Ilcsoftpackage):
    """ Kaltest tracking software. """

    homepage = "https://github.com/iLCSoft/KalTest"
    url      = "https://github.com/iLCSoft/KalTest/archive/v02-05.tar.gz"
    git      = "https://github.com/iLCSoft/KalTest.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('2.5',      sha256='8753ecf5ed7819744cc66a652cf8ddcd0d783a25ee19b5387212f70dd9abbce5')
    version('2.4',      sha256='8cd089a51c499cc807dda196150a3da124b4a2a192bcc6b2d55b9c8b5481e5d5')
    version('2.3',      sha256='fa09a8e4a29c18b7b7b094d5d675a70b15eca1a9871c64141bafb9da0b893d3e')
    version('2.2',      sha256='af0a2bbb842c83dc9dcd9717ae836d1f3bc4207730d0bd18d1264d8958b79e95')
    version('2.1',      sha256='2bf0e0407a7de5c4a59c722027daea46967c60e9e9bcfc7d4fa22d2127360e7c')
    version('2.0',      sha256='46b02bbea72e44c4309faa7e6d419b7ae103845125c8e4e9f3de864cba766e58')

    depends_on('ilcutil')
    depends_on('root')

    patch("dict.patch")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def setup_run_environment(self, spack_env):
        # The dictionary headers required kaltest to be in CPATH or ROOT_INCLUDE_PATH
        # other libraries require include to be searchable (which is automatic)
        spack_env.prepend_path('CPATH', self.prefix.include.kaltest)

    def url_for_version(self, version):
        return ilc_url_for_version(self, version)
