# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Aidatt(CMakePackage):
    """Tracking toolkit developed in the AIDA project."""

    homepage = "https://github.com/AIDASoft/aidaTT"
    url      = "https://github.com/AIDASoft/aidaTT/archive/v00-10.tar.gz"
    git      = "https://github.com/AIDASoft/aidaTT.git"

    maintainers = ['vvolkl']

    version("master", branch="master")
    version('0.10.0',     sha256='5379a369ee29bebeece7e814c0595bac9f08f2737ce03ae529b4b4e84dea1283')

    variant('gbl', default=False,
            description="Build with GeneralBrokenLines")
    variant('lcio', default=False,
            description="Build with LCIO")
    variant('dd4hep', default=False,
            description="Build with DD4hep")

    depends_on('ilcutil')
    depends_on('eigen')
    depends_on('generalbrokenlines', when="+gbl")
    depends_on('dd4hep', when="+dd4hep")
    depends_on('lcio', when="+lcio")
