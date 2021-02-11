# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class K4simdelphes(CMakePackage):
    """EDM4HEP output for Delphes."""

    homepage = "https://github.com/key4hep/k4SimDelphes"
    git      = "https://github.com/key4hep/k4SimDelphes.git"
    url      = "https://github.com/key4hep/k4SimDelphes/archive/v00-00-01.tar.gz"

    maintainers = ['vvolkl']

    version('main', branch='main')
    version('0.1.2', sha256='c36a123ace6150c05d4b1114b532cf2a3a1b63e96f706a84bed849fd61f0def7')
    version('0.0.1', sha256='4bc414ac72cd03638e7f406381b41814f6e19f3425051f094ac0b539630cd698')

    patch('cmake2.patch', when="@0.0.1")

    variant('framework', default=True, description="Build Gaudi framework integration.")
    variant('integration_tests', default=True, description="Enable integration tests for framework.")
    variant('delphes_pythia', default=True, description='Build standalone executable with Pythia input.')
    variant('delphes_hepmc', default=True, description='Build standalone executable with Hepmc input.')
    variant('delphes_pythia_evtgen', default=True, description='Build standalone executable with Pythia+EvtGen input')

    depends_on('edm4hep')
    depends_on('delphes@3.4.3pre08:')
    depends_on('pythia8', when="+delphes_pythia")
    depends_on('evtgen+pythia8', when="+delphes_pythia_evtgen")
    depends_on('hepmc', when="+delphes_hepmc")
    depends_on('k4fwcore', when="+framework")

    depends_on('catch2@3.0.1:', type=('test'))
    depends_on('k4gen', when="+integration_tests", type=('test'))

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_FRAMEWORK", 'framework'),
            self.define_from_variant("BUILD_PYTHIA_READER", 'delphes_pythia'),
            self.define_from_variant("BUILD_HEPMC_READER", 'delphes_hepmc'),
            self.define_from_variant("BUILD_EVTGEN_READER", 'delphes_pythia_evtgen'),
            self.define("USE_EXTERNAL_CATCH2", True),
        ]
        return args

    def setup_build_environment(self, env):
        env.set('PYTHIA8', self.spec["pythia8"].prefix)

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
