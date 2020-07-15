# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Gear(CMakePackage):
    """ Linear Collider Conditions Data toolkit."""

    homepage = "https://github.com/iLCSoft/gear"
    git      = "https://github.com/iLCSoft/gear.git"
    url      = "https://github.com/iLCSoft/gear/archive/v01-05.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.9.0', sha256='18564d50bc4863441bd4b5b72dda565065f8b7f5821e30c804c7e93c7afe84ae')

    variant('tgeo', default=False,
            description="builds with ROOT tgeo")

    variant('doc', default=False,
            description="build doxygen documentation")


    depends_on("ilcutil")
    depends_on("clhep")
    depends_on("root", when="+tgeo")
    depends_on("doxygen", when="+doc")


    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define_from_variant('GEAR_TGEO', 'tgeo'))
        args.append(self.define_from_variant('INSTALL_DOC', 'doc'))
        args.append('-DCMAKE_CXX_STANDARD=17')
        return args

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
