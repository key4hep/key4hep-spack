# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Ddkaltest(CMakePackage):
    """Interface between KalTest fitter and DD4hep based geometry"""

    homepage = "https://github.com/iLCSoft/DDKalTest"
    url      = "https://github.com/iLCSoft/DDKalTest/archive/v01-06.tar.gz"
    git      = "https://github.com/iLCSoft/DDKalTest.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.6',     sha256='e668242d84eb94e59edca18e524b1a928fcf7ae7c4b79f76f0338a0a4e835d8f')
    version('1.5',     sha256='4ef6fea7527dbb5f9a12322e92e27d80f2c29b115aae13987f55cb6cf02f31f5')
    version('1.4',     sha256='c5cefd23366c47087a6b04b5d48ab28ac88e8855446d782cfb8a954088fd4207')
    version('1.3',     sha256='77615c119bb930b9f447c6d7f0e94dbd51e34115fc30d5625f9f32c1b8fee886')
    version('1.2',     sha256='8f65466c22fc46d4414ecba7470a5e997a7510ceeae1f8eca1f0c5998d4418d9')
    version('1.1',     sha256='e36e519259dd0994a4ef67618b59d7aff6f68898ad28160d2c196c0281179870')
    version('1.0',     sha256='0780a698eb8a1df9b931da7bdb89de6177d97361d3cb1d5353eb1a382cd5a59c')

    depends_on('dd4hep')
    depends_on('root')
    depends_on('ilcutil')
    depends_on('lcio')
    depends_on('gsl')
    depends_on('kaltest')
    depends_on('aidatt')
    
    @run_after('install')
    def installheaders(self):
      #make('install')
      install_tree('.', self.prefix)
    
    def url_for_version(self, version):
       return ilc_url_for_version(self, version)
