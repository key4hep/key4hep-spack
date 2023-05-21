# ----------------------------------------------------------------------------

from spack.pkg.k4.key4hep_stack import Key4hepPackage 


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

    version('master', branch='master')
    version('0.2.6', sha256='4fd46326154a13f89a39ca98d23253542b78de7abac572808fa59f929566e02a')
    version('0.2.5', sha256='fb0aa15a3895fe822f936936b810205e9330a9ffe763be16a225fc5e9580bd2c')
    version('0.2.4', sha256='86802d09da1feca8fdfaf947ccad762e28dd91644669c1a057ac4df748e807c9')
    version('0.2.3', sha256='38254b2beeb8eb6de81e2dfa94b7c9f1b307fe512dc4fec9c3691f359509d008')
    version('0.2.2', sha256='634bc0ce54a82ddaac43dd37d504bf1ea390dcdd30f9ebfd2264fc7073e37fea')
    version('0.2.1', sha256='32ca07da4e655094c1a861f86a7766f197dd4a3e8a7a82bd9dd2f2539188ad8e')
    version('0.2.0', sha256='1ca9823ef4492c25e776de9f2f4884ed9068f907b4e080342276d92ad4071af6')


    patch('https://github.com/vvolkl/CEPCSW/commit/42f64d710fb25af363e2ed9a18b94bae1537a20f.patch',
          sha256='87bf94536f5fd7fb675ca4eff25277331b7de94ef541f2bd8ea178a5e61fd20d', when="@0.2.1")

    depends_on('clhep')
    depends_on('dd4hep')
    depends_on('edm4hep')
    depends_on('podio')
    depends_on('k4fwcore@1.0pre14:', when='@0.2.4:')
    depends_on('k4fwcore@0.3.0:')
    depends_on('garfieldpp', when='@0.2.1:')
    depends_on('gaudi@35.0:')
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

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
