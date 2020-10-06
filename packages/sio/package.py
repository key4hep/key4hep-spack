# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, Ilcsoftpackage


class Sio(CMakePackage):
    """SIO is a persistency solution for reading and writing binary data in SIO structures called record and block. SIO has originally been implemented as persistency layer for LCIO."""

    url      = "https://github.com/iLCSoft/SIO/archive/v00-00-02.tar.gz"
    homepage = "https://github.com/iLCSoft/SIO"
    git      = "https://github.com/iLCSoft/SIO.git"

    maintainers = ['vvolkl']

    version('master', branch="master")
    version('0.0.2', sha256='e4cd2aeaeaa23c1da2c20c5c08a9b72a31b16b7a8f5aa6d480dcd561ef667657')



    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
