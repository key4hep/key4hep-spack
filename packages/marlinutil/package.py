# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Marlinutil(CMakePackage):
    """ Library that containes classes and functions that are used by more
    than one processor. In particular it contains the geometry classes that
    are used until we have the geometry for reconstruction package (GEAR)."""

    homepage = "https://github.com/iLCSoft/MarlinUtil/"
    url      = "https://github.com/iLCSoft/MarlinUtil/archive/v01-15-01.tar.gz"
    git      = "https://github.com/iLCSoft/MarlinUtil.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('01-15-01',  sha256='05e878c9aae4a675e37ad2c63abc0b1c4c2a45dcb2e3c9ae5c31e7e6f64118bf')
    version('01-15',     sha256='61c75248e0750c5dcd75995ac9400c29e9e5d60c510a72d8c813d96c0c787c99')
    version('01-14',     sha256='85a628461ce77c62b2815a70719830970569fe22d973c218b0ef1a7ed37c5366')
    version('01-13-pre', sha256='d3b37d99313138a82335a43b6febe54b7e5b20551cf119004555e8086432b667')
    version('01-13',     sha256='61826642fc95d01d867a2dfda612f1c2126e2cb92bcf20a87cbe8d791453db91')
    version('01-12-01',  sha256='812a694bf16158d33c6e3b0fe4e5b4ced315c563ef7963accaf1aa0d1f170b23')
    version('01-12',     sha256='649145b926e2dc9a837b97c37c0471d77d87a27caea499f764b2aba9c6544216')
    version('01-11',     sha256='7b025d8bb702839c43c6cd35962cd4f13fedadc210f859233d3cdd2faeadbcb1')
    version('01-10',     sha256='8db3d61a31f9d462e533e2ea335922663360641174cc6341dd95c6e86dd37725')
    version('01-09',     sha256='98f8f49dcfe65a79b5638a0e039831b7e95b3ff649064aaab987b6190f02cd2b')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('clhep')
    depends_on('gsl')
    depends_on('ced')
    depends_on('dd4hep')
    depends_on('root')
