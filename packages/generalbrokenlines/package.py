# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install generalbrokenlines
#
# You can edit this file again by typing:
#
#     spack edit generalbrokenlines
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Generalbrokenlines(CMakePackage):
    """Track refitting with broken lines in 3D."""

    homepage = "https://github.com/GeneralBrokenLines/GeneralBrokenLines"
    url      = "https://github.com/GeneralBrokenLines/GeneralBrokenLines/archive/V02-02-00.tar.gz"
    git      = "https://github.com/GeneralBrokenLines/GeneralBrokenLines.git"

    maintainers = ['vvolkl']

    version("master", branch="master")
    version('02-02-00', sha256='81237239415d9c0ee05223c035f22353880084121b587c384ebd0a5754677dfc')
    version('02-01-03', sha256='f96bc7ae5e5d1199517598a44c293b793e5d8e987e1737fae0b67ffc1f8c4f9f')
    version('02-01-02', sha256='a0a81c0682501016df8a0760234138e4546c88dbafa40ef29050d2929bdc9827')
    version('02-01-01', sha256='21fe55d7aee2022a8f7d873c3b191ad334915d643956f18004a6d967d22d3e39')
    version('02-01-00', sha256='27fe33529447b1976ecbdcafaabd1aeab072b5773685a89d6c0f3ac10fd2b920')
    version('02-00-01', sha256='351625b17d51ca6631c7901dcebad80b328def5f05f46b194f1990f547f1e248')
    version('02-00-00', sha256='58ca3e1da1cc198da5bdef9c893c622475fbc145bdd6e2ebcd92e763abcda838')
    version('01-18-00', sha256='1e08bd97bfd6bb4afc165cd960f7e68199085f40bb368163db8885a529c4017e')
    version('01-17-01', sha256='66afdce406f7e7fe06c3faeadd73d651e39b9a2d60d0207b816bc2798159208d')
    version('01-17-00', sha256='f0cd628fd734fc7228ff25bfd20958a7ae4fc2c290796957b3790e617143f56a')


    depends_on('eigen')
    depends_on('root', when="+root")

    def cmake_args(self):
        args = [ self.define_from_variant("SUPPORT_ROOT", "root") ]
        return args
