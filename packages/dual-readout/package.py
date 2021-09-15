# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage, k4_add_latest_commit_as_version


class DualReadout(CMakePackage, Key4hepPackage):
    """Repository for GEANT4 simulation & analysis of the dual-readout calorimeter """

    url      = "https://github.com/HEP-FCC/dual-readout/archive/v0.0.2.tar.gz"
    homepage = "https://github.com/HEP-FCC/dual-readout"
    git      = "https://github.com/HEP-FCC/dual-readout.git"

    maintainers = ['vvolkl', 'SanghyunKo']

    version('master', branch='master') 
    version('0.0.3', sha256='d35e7193c11385505494f11328d54a595b3ff953563bae06b8954c1ef24209b3')
    version('0.0.2', sha256='f76c1febf3d8e29d5287ba03eacbc244f8c615502295f7471579245376da91ad')

    depends_on('dd4hep+geant4')
    depends_on('hepmc3+rootio')
    depends_on('fccsw')
    depends_on('fastjet')
    depends_on('root')
    depends_on('pythia8')
    depends_on('hsf-cmaketools')

    def cmake_args(self):
        args = []
        # C++ Standard
        #args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
          args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

    def setup_build_environment(self, env):
        env.set('PYTHIA8_ROOT_DIR', self.spec["pythia8"].prefix)

