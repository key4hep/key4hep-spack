# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Key4hepPackage


class DualReadout(CMakePackage, Key4hepPackage):
    """Repository for GEANT4 simulation & analysis of the dual-readout calorimeter """

    url      = "https://github.com/HEP-FCC/dual-readout/archive/v0.0.2.tar.gz"
    homepage = "https://github.com/HEP-FCC/dual-readout"
    git      = "https://github.com/HEP-FCC/dual-readout.git"

    maintainers = ['vvolkl', 'SanghyunKo']

    version('master', branch='master') 
    version('0.1.0', sha256='f4b9387ccae0d4d364b1340eb116c5b4b93a6bc74c896fcd221619ddec31d5f6')
    version('0.0.3', sha256='d35e7193c11385505494f11328d54a595b3ff953563bae06b8954c1ef24209b3')
    version('0.0.2', sha256='f76c1febf3d8e29d5287ba03eacbc244f8c615502295f7471579245376da91ad')

    depends_on('dd4hep')
    depends_on('edm4hep@0.4.1:', when='@0.1.0:')
    depends_on('podio@0.14.1:', when='@0.1.0:')
    depends_on('py-jinja2', type=('build'))
    depends_on('py-pyyaml', type=('build'))
    depends_on('hepmc3+rootio')
    depends_on('fastjet')
    depends_on('root')
    depends_on('pythia8')
    depends_on('hsf-cmaketools')
    depends_on('k4fwcore')
    depends_on('k4fwcore@1.0pre14:', when='@0.1.0:')
    depends_on('simsipm', when='@0.1.0:')

    # fix ambiguous issue on clang
    # https://stackoverflow.com/questions/40221969/overloaded-operator-ambiguity-on-clang-but-not-on-gcc-which-one-is-correct
    patch('clang.patch')
    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
          args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

    def setup_build_environment(self, env):
        env.set('PYTHIA8_ROOT_DIR', self.spec["pythia8"].prefix)
        
    def setup_run_environment(self, env):
        env.set('DUALREADOUT', self.spec.prefix)
