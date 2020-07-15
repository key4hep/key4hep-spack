# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Marlintrk(CMakePackage):
    """Tracking Package based on LCIO and GEAR,
       primarily aimed at providing track fitting in Marlin."""

    homepage = "https://github.com/iLCSoft/MarlinTrk"
    url      = "https://github.com/iLCSoft/MarlinTrk/archive/v02-08.tar.gz"
    git      = "https://github.com/iLCSoft/MarlinTrk.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('2.8',     sha256='bd3b0074c06e2b778c74d1aeb2c989c39100a8adf5018792db599f84cb946c14')
    version('2.7',     sha256='c6e556d18ae6f2f3ae6c0fd8aa4322ce866e08b54b48ce95d09636443eff53ea')
    version('2.6',     sha256='a7be303a775eeb1a7b91f17710669878da9a6d4cca16aed1d251e63a8885c7fd')
    version('2.5',     sha256='b5174986160315a62adba29f64fad2a27c8a7f53754a6b55740ea74f212cf9da')
    version('2.4',     sha256='f77556cee804ec4ddd74dd229685fac07a462178b33b629f26cacbf4336c7cb7')
    version('2.3',     sha256='6240a09c259b4632658fa43bbb5e6d0248c0d8b706fb54cbac563ab3aa5a7d58')
    version('2.2',     sha256='15515259f422ba23cb9f717834fb6d1e3e3ee9ca4ad17c04dd5efd8aa1c16113')
    version('2.1',     sha256='a721c9b871b234be1decc88cabf5125b959a971ede74b9c2c368a505a1c6718e')

    variant('gear', default=False,
            description="Provide Gear backward compatibility")

    depends_on('ilcutil')
    depends_on('lcio')
    depends_on('gear', when="+gear")
    depends_on('kaltest')
    depends_on('kaldet')
    depends_on('root')
    depends_on('ddkaltest')
    depends_on('clhep')
    depends_on('aidatt')
    depends_on('gsl')
    depends_on('generalbrokenlines')

    def cmake_args(self):
        args = [self.define_from_variant("MARLINTRK_USE_GEAR", "gear")]
        return args
        
    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
