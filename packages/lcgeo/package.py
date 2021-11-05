# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Ilcsoftpackage, k4_add_latest_commit_as_version


class Lcgeo(CMakePackage, Ilcsoftpackage):
    """DD4hep geometry models for future colliders."""

    homepage = "https://github.com/iLCSoft/lcgeo"
    git      = "https://github.com/iLCSoft/lcgeo.git"
    url      = "https://github.com/iLCSoft/lcgeo/archive/v00-16-06.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.16.7', sha256='bde23af3c8dc695c4dcbb7460764c23e75dc534cd8a6170190e50a1a8083d45c')
    version('0.16.6', sha256='0eef7137ad69b771e5cf8a3f4a71e060e9d57ee825d8d944fa6a0dec8c2dad60')
    version('0.16.5', sha256='a46738b2479c0469b06584f82801bf2dd546623180300753de0b5684abd12a05')

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('lcio')
    depends_on('dd4hep +geant4')
    depends_on('boost')
    depends_on('root')


    def cmake_args(self):
        args = []  
        args.append(self.define_from_variant('CMAKE_CXX_STANDARD', 'cxxstd'))
        args.append(self.define('BUILD_TESTING', self.run_tests))
        return args


    @run_after('install')
    def install_compact(self):
        install_tree('CaloTB', self.prefix.share.lcgeo.compact.CaloTB)
        install_tree('CLIC', self.prefix.share.lcgeo.compact.CLIC)
        install_tree('FCalTB', self.prefix.share.lcgeo.compact.FCalTB)
        install_tree('FCCee', self.prefix.share.lcgeo.compact.FCCee)
        install_tree('fieldmaps', self.prefix.share.lcgeo.compact.fieldmaps)
        install_tree('ILD', self.prefix.share.lcgeo.compact.ILD)
        install_tree('SiD', self.prefix.share.lcgeo.compact.Sid)

    def setup_run_environment(self, env):
        env.set('LCGEO', self.prefix.share.lcgeo.compact)
        env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.set('LCGEO', self.prefix.share.lcgeo.compact)
        spack_env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib64)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')
