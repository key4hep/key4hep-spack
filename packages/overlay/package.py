# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Overlay(CMakePackage):
    """The package Overlay provides code for event overlay with Marlin."""

    url      = "https://github.com/iLCSoft/Overlay/archive/v00-22.tar.gz"
    homepage = "https://github.com/iLCSoft/Overlay"
    git      = "https://github.com/iLCSoft/Overlay.git"

    maintainers = ['vvolkl']

    version('0.22', sha256='fa03e2870b8f072fd9c1cd68354274437050ce6ed30d0db9a816a3cbdee54cb1')

    depends_on('ilcutil')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('clhep')
    depends_on('raida')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libOverlay.so")

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
