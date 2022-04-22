# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

from spack.pkg.k4.key4hep_stack import Key4hepPackage

class K4edm4hep2lcioconv(CMakePackage, Key4hepPackage):
    """Converter library between EDM4hep and LCIO"""

    homepage = "https://github.com/key4hep/k4EDM4hep2LcioConv"
    git      = "https://github.com/key4hep/k4EDM4hep2LcioConv.git"
    url      = "https://github.com/key4hep/k4EDM4hep2LcioConv/archive/refs/heads/master.zip"

    maintainers = ['fdplacido']

    version('master', branch='master')

    depends_on('lcio')
    depends_on('podio')
    depends_on('edm4hep@0.4.1:')

    def cmake_args(self):
      args = [
        self.define("BUILD_TESTING", self.run_tests)
      ]
      args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
      return args

    def setup_run_environment(self, spack_env):
      spack_env.set("K4EDM4HEP2LCIOCONV", self.prefix.share.k4EDM4hep2LcioConv)

    # def setup_build_environment(self, spack_env):
      # spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['k4edm4hep2lcioconv'].prefix + '/lib')
      # spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['k4edm4hep2lcioconv'].prefix + '/lib64')
      # Try without, if missing then putit
      # k4_setup_env_for_framework_tests(self.spec, env)
