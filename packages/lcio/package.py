# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Lcio(CMakePackage):
    """HEP Library for Linear Collider Input/Output"""

    homepage = "http://lcio.desy.de"
    git      = "https://github.com/iLCSoft/LCIO.git"
    url      = "https://github.com/iLCSoft/LCIO/archive/v02-13-03.tar.gz"

    maintainers = ['gaede', 'vvolkl']

    version('master', branch='master')
    version('2.13.3', sha256='35aaa7989be33574a7c44ea7e6d7780ab26ef8bd4aa29d495f3831a3cd269304')
    version('2.13.2', sha256='9f153ba13e56ee16795378f9192678d40df1faca51d00aaa8fb80547bfecb8d8')

    variant('cxxstd',
            default='17',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')
    variant("jar", default=False,
    description="Turn on to build/install lcio.jar")
    variant("rootdict", default=True,
    description="Turn on to build/install ROOT dictionary.")
    variant("examples", default=False,
    description="Turn on to build LCIO examples")

    depends_on('root@6.04:', when="+rootdict")
    depends_on('openjdk', when="+jar")
    # build error with +termlib, to be investigated
    depends_on('ncurses~termlib', when="+examples")
    depends_on('readline', when="+examples")


    def cmake_args(self):
        args = [
            self.define('CMAKE_CXX_STANDARD', self.spec.variants['cxxstd'].value),
            self.define('BUILD_TESTING', self.run_tests),
            self.define_from_variant("BUILD_LCIO_EXAMPLES", 'examples'),
            self.define_from_variant("BUILD_ROOTDICT", 'rootdict'),
            self.define_from_variant("INSTALL_JAR", 'jar'),
        ]
        return args

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
