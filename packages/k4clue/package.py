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

    depends_on('cupla')
    depends_on('alpaka')
    depends_on('k4fwcore')
    depends_on('dd4hep')


    def cmake_args(self):
        args = []
        args.append(self.define('cupla_DIR', self.spec['cupla'].prefix))
        return args

    def setup_run_environment(self, spack_env):
        spack_env.set("K4CLUE", self.prefix.share.k4Clue)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)

    
    def setup_build_environment(self, env):
        k4_setup_env_for_framework_tests(self.spec, env)
        env.prepend_path("CPATH", self.spec['dd4hep'].prefix.include)
        env.prepend_path("CPATH", self.spec['alpaka'].prefix.include)

