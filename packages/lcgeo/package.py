# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lcgeo(CMakePackage, Ilcsoftpackage):
    """DD4hep geometry models for future colliders."""

    homepage = "https://github.com/iLCSoft/lcgeo"
    git      = "https://github.com/iLCSoft/lcgeo.git"
    url      = "https://github.com/iLCSoft/lcgeo/archive/v00-16-07.tar.gz"

    generator = 'Ninja'

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.16.8', sha256='e729e678a2a2105b58b30b0110cc910edb95e02c8b6babbb9f8d74041d5a0c55')
    version('0.16.7', tag='v00-16-07')
    version('0.16.6', sha256='0eef7137ad69b771e5cf8a3f4a71e060e9d57ee825d8d944fa6a0dec8c2dad60')
    version('0.16.5', sha256='a46738b2479c0469b06584f82801bf2dd546623180300753de0b5684abd12a05')

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('lcio')
    depends_on('dd4hep')
    depends_on('lcio')
    depends_on('boost')
    depends_on('root')
    depends_on('python', type='build')
    depends_on('ninja', type='build')

    patch('https://github.com/iLCSoft/lcgeo/commit/cb87609446255c3a94da867ad7801a62ff3b6b05.patch',
          sha256='3e02ca5c89558342d8fd2489463c285af5a5500baeba2faf8d41f8ec3ae2f487',
          when='@0.16.7')


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

    def setup_build_environment(self, env):
        env.set('LCGEO', self.prefix.share.lcgeo.compact)
        env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.set('LCGEO', self.prefix.share.lcgeo.compact)
        spack_env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib64)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')

    # dd4hep tests need to run after install step:
    # disable the usual check
    def check(self):
        pass

    # instead add custom check step that runs after installation
    @run_after('install')
    def install_check(self):
        print(self)
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja('test')

