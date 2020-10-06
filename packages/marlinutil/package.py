# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Marlinutil(CMakePackage):
    """ Library that containes classes and functions that are used by more
    than one processor. In particular it contains the geometry classes that
    are used until we have the geometry for reconstruction package (GEAR)."""

    homepage = "https://github.com/iLCSoft/MarlinUtil/"
    url      = "https://github.com/iLCSoft/MarlinUtil/archive/v01-15-01.tar.gz"
    git      = "https://github.com/iLCSoft/MarlinUtil.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.15.1',  sha256='05e878c9aae4a675e37ad2c63abc0b1c4c2a45dcb2e3c9ae5c31e7e6f64118bf')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('clhep')
    depends_on('gsl')
    depends_on('ced')
    depends_on('dd4hep')
    depends_on('root')

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
