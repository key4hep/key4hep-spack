# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


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

