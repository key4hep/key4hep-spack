# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4clue(CMakePackage, Key4hepPackage):
    """CLUE Clustering for Key4hep"""

    url      = "https://github.com/key4hep/k4Clue"
    git      = "https://github.com/key4hep/k4Clue.git"
    homepage = "https://github.com/key4hep/k4Clue"

    maintainers = ['vvolkl']

    version('main', branch='main')

    patch('https://github.com/vvolkl/k4Clue/commit/278740f7eb0074ebb0e72e51da3ccefec1fbba13.patch',
          sha256='f806279323bd56cb3b58a05ee4873efa8c2395b16b18cbaeb3bda12ee6510052')

    depends_on('cupla')
    depends_on('alpaka')
    depends_on('k4fwcore')
    depends_on('dd4hep')
    depends_on('py-six', type=('build', 'run'))

    # todo: fix type='test'
    depends_on('marlindd4hep')
    depends_on('kaltest')
    depends_on('conformaltracking')
    depends_on('overlay')
    depends_on('marlinreco')
    depends_on('marlintrkprocessors')
    depends_on('ddmarlinpandora')
    depends_on('fcalclusterer')
    depends_on('lctuple')
    depends_on('marlinfastjet')
    depends_on('lcfiplus')
    depends_on('k4marlinwrapper')

    def cmake_args(self):
        args = []
        args.append(self.define('cupla_DIR', self.spec['cupla'].prefix))
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("K4CLUE", self.prefix.share.k4Clue)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)
        spack_env.prepend_path("CPATH", self.spec['cupla'].prefix.include)
        spack_env.prepend_path("CPATH", self.spec['alpaka'].prefix.include)

    
    def setup_build_environment(self, env):
        k4_setup_env_for_framework_tests(self.spec, env)
        env.prepend_path("CPATH", self.spec['dd4hep'].prefix.include)
        env.prepend_path("CPATH", self.spec['alpaka'].prefix.include)

