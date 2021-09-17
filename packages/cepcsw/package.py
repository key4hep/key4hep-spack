# ----------------------------------------------------------------------------

from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage, k4_add_latest_commit_as_version 


class Cepcsw(CMakePackage, Key4hepPackage):
    """CEPC offline experiment software based on Key4hep."""

    homepage = "https://github.com/cepc/CEPCSW"
    url      = "https://github.com/cepc/CEPCSW/archive/v0.1.tar.gz"
    git      = "https://github.com/cepc/CEPCSW.git"

    maintainers = ['mirguest']


    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    k4_add_latest_commit_as_version(git)
    version('master', branch='master')
    version('0.1.1', sha256='0d56c2e63c0d91a64854c44ab4c0575fb0646cb566113721e3f35aee24e6a334')
    version('0.1.2', sha256='2caaf0723fa2561e97eb303e245b6a5e25185d4195b48c6a30dcc8d315951f42')
    version('0.2.0', sha256='1ca9823ef4492c25e776de9f2f4884ed9068f907b4e080342276d92ad4071af6')
    version('0.2.1', sha256='32ca07da4e655094c1a861f86a7766f197dd4a3e8a7a82bd9dd2f2539188ad8e')
    patch('https://github.com/vvolkl/CEPCSW/commit/42f64d710fb25af363e2ed9a18b94bae1537a20f.patch',
          sha256='87bf94536f5fd7fb675ca4eff25277331b7de94ef541f2bd8ea178a5e61fd20d', when="@0.2.1")

    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('edm4hep')
    depends_on('k4fwcore@0.3.0:', when='@0.2:')
    depends_on('k4fwcore@0.2.0', when='@:0.1.99')
    depends_on('garfieldpp', when='@0.2.1:')
    depends_on('gaudi@:34.99', when='@:0.1.99')
    depends_on('gaudi@35.0:', when='@0.2:')
    depends_on('gear')
    depends_on('genfit')
    depends_on('lcio')
    depends_on('lccontent')
    depends_on('hepmc')
    depends_on('pandorasdk')
    depends_on('pandorapfa')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
            args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append('-DCMAKE_MODULE_PATH=%s'%cmake_modules)
        return args
    def flag_handler(self, name, flags):
        if name == 'cxxflags':
            flags.append('-Wno-c++11-narrowing')
        return (flags, None, flags)

