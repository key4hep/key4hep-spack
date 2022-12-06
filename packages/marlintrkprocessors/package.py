# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlintrkprocessors(CMakePackage, Ilcsoftpackage):
    """A collection of Tracking Relelated Processors Based on MarlinTrk"""

    url      = "https://github.com/iLCSoft/MarlinTrkProcessors/archive/v02-11.tar.gz"
    homepage = "https://github.com/iLCSoft/MarlinTrkProcessors"
    git      = "https://github.com/iLCSoft/MarlinTrkProcessors.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version("2.12.2", sha256="862ed161a882f6b3bc14033be8a38fa9a126594da3774194092adb1c69a0b5e5")
    version('2.12.1', sha256='677532d8d7c9a8489be091d249c8893e2bfb66c78d0e1537cafff97456a00bf5')
    version('2.12', sha256='ac1a3af380c837868649c8b7767e7641d25a1ecf40690726d55a9bcc58a54640')
    version('2.11', sha256='49a567831e2b7a0c43ded955ce31fbe7d467a59960f4bcc2c2120e20762639b0')

    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('ddkaltest')
    depends_on('raida')


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinTrkProcessors.so")

    def cmake_args(self):
        return [
            self.define('CMAKE_CXX_STANDARD',
                        self.spec['root'].variants['cxxstd'].value)
        ]
