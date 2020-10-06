# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Raida(CMakePackage):
    """ A utility package for the iLCSoft software framework """

    homepage = "https://github.com/iLCSoft/raida"
    git      = "https://github.com/iLCSoft/raida.git"
    url      = "https://github.com/iLCSoft/raida/archive/v01-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.9.0', sha256='53ad3fd7c62e5eba70e6d6099e5ef4d92920399afb7b31dc8008b6ad865a9e85')


    depends_on('ilcutil')
    depends_on("root")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'
                    % self.spec['root'].variants['cxxstd'].value)
        args.append('-DBUILD_TESTING=%s' % self.run_tests)
        return args

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
