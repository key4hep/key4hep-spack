# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Ilcutil(CMakePackage, Ilcsoftpackage):
    """ A utility package for the iLCSoft software framework """

    homepage = "https://github.com/iLCSoft/ilcutil"
    git      = "https://github.com/iLCSoft/ilcutil.git"
    url      = "https://github.com/iLCSoft/ilcutil/archive/v01-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.6.2', sha256='2bb018f8cca4ca2480ba00c1f16100e62094fa6f9a0f07d2ba3a3dc274e32f3c')
    version('1.6.1', sha256='cb51f110c0c7b6e5732ab66d49b4658c56bb5944c1540f1563612ac56bb70823')
    version('1.6', sha256='09083890721704f39a3e902dc660db5326027cc38446b813233d04ec3233ba2e')

    patch("installdoc.patch", when="@:1.6.1")

    variant('cxxstd',
            default='17',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    variant('doc', default=False, description='Build the documentation')

    depends_on("doxygen", when="+doc")

    def cmake_args(self):
        # C++ Standard
        return [
            self.define_from_variant('CMAKE_CXX_STANDARD', 'cxxstd'),
            self.define_from_variant('INSTALL_DOC', 'doc')
        ]
