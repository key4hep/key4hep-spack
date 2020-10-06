# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Overlay(CMakePackage):
    """The package Overlay provides code for event overlay with Marlin."""

    url      = "https://github.com/iLCSoft/Overlay/archive/v00-22.tar.gz"
    homepage = "https://github.com/iLCSoft/Overlay"
    git      = "https://github.com/iLCSoft/Overlay.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.22.1',   sha256='2f3ca472fe6aae44cdae0553f0e65b3c086a0d887d9cf53fd19468fb6107155b')
    version('0.22',     sha256='fa03e2870b8f072fd9c1cd68354274437050ce6ed30d0db9a816a3cbdee54cb1')
    version('0.21',     sha256='b64bac24d8218f33b871aa232e994a3e12c8a0c7862789b09f9ca189ae20d8c4')
    version('0.20',     sha256='f8baa3d17b1382cdcb8d3fdff34cbbe0c510885a1b94aee4dcdb61c10dc3520d')
    version('0.19',     sha256='0d946ab3e3e225dc49608772823997396a7999501ad140717acc4a6d09136a94')
    version('0.18',     sha256='8f1bbacfd04400328f7be42d342cc8df84f8627b540d24c789decc178ba08d65')
    version('0.17-pre', sha256='0aff5f8c509148832590df847e928899dcec2cdef153a8d0e0d694994ae318fe')
    version('0.17',     sha256='050c678520a01d92d12bc2256807e5aa37614097e3269ed219b56689e1b731ab')
    version('0.16',     sha256='9ade6b4920256275a3bdecb9315ab700c99facbb79b9fb374afac8fc83967430')
    version('0.15',     sha256='fa16f66bef0325f63d733214ed98bbc60225a99c039e39139609fef262a124a0')
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
