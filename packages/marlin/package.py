# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Marlin(CMakePackage):
    """ Linear Collider framework"""

    homepage = "https://github.com/iLCSoft/marlin"
    git      = "https://github.com/iLCSoft/marlin.git"
    url      = "https://github.com/iLCSoft/marlin/archive/v01-05.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.17.0', sha256='076acc3a91b7e2e253f338395a8e56bf00498e6aa1a118d3e7bde84f1065d3d6')


    variant('gui', default=False,
            description="builds with qt gui")

    variant('lccd', default=True,
            description="builds with lccd")

    variant('clhep', default=True,
            description="builds with lccd")

    variant('aida', default=True,
            description="builds with lccd")

    variant('doc', default=False,
            description="build doxygen documentation")


    depends_on("ilcutil")
    depends_on("gear")
    depends_on("lcio")
    depends_on("doxygen", when="+doc")
    depends_on("qt4", when="+gui")
    depends_on("lccd", when="+lccd")
    depends_on("clhep", when="+clhep")
    depends_on("aida", when="+aida")


    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define_from_variant('INSTALL_DOC', 'doc'))
        args.append(self.define_from_variant('MARLIN_GUI', 'gui'))
        args.append(self.define_from_variant('MARLIN_LCCD', 'lccd'))
        args.append(self.define_from_variant('MARLIN_LCCD', 'clhep'))
        args.append(self.define_from_variant('MARLIN_AIDA', 'aida'))
        args.append('-DCMAKE_CXX_STANDARD=17')
        if 'aida' in self.spec:
          args.append('-DAIDA_DIR=%s' % self.spec["aida"].prefix)
        return args

    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/iLCSoft/marlin/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/iLCSoft/marlin/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

