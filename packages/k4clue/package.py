# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4clue(CMakePackage, Key4hepPackage):
    """CLUE Clustering for Key4hep"""

    url      = "https://github.com/key4hep/k4Clue/archive/v01-00.tar.gz"
    git      = "https://github.com/key4hep/k4Clue.git"
    homepage = "https://github.com/key4hep/k4Clue"

    maintainers = ("vvolkl", "jmcarcell")

    version('main', branch='main')

    version("1.0.1", sha256="e6977ca0b4d841116a2c2d7755ce2373ff30624ecb66c1b3b4514b5127886616")
    version("1.0.0", sha256="b1b1c871a2425305e56c1923c31eded300a28cd1a97c55e8b440caaefcafc7d1")

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

