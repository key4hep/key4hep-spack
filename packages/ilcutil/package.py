# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Ilcutil(CMakePackage):
    """ A utility package for the iLCSoft software framework """

    homepage = "https://github.com/iLCSoft/ilcutil"
    git      = "https://github.com/iLCSoft/ilcutil.git"
    url      = "https://github.com/iLCSoft/ilcutil/archive/v01-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.6', sha256='09083890721704f39a3e902dc660db5326027cc38446b813233d04ec3233ba2e')

    patch("installdoc.patch")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
