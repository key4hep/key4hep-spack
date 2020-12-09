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
    version('0.0.1', sha256='4bc414ac72cd03638e7f406381b41814f6e19f3425051f094ac0b539630cd698')

    patch('cmake2.patch', when="@0.0.1")

    depends_on('edm4hep')
    depends_on('delphes@3.4.3pre06:')
    depends_on('pythia8')
    depends_on('evtgen+pythia8')
    depends_on('hepmc')

    def setup_build_environment(self, env):
        env.set('PYTHIA8', self.spec["pythia8"].prefix)

    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
