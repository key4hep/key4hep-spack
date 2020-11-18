
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version


class Edm4hep(CMakePackage, Ilcsoftpackage):
    """Event data model of Key4HEP"""

    homepage = "https://github.com/key4hep/EDM4hep"
    url = "https://github.com/key4hep/EDM4hep/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/EDM4hep.git"

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.2.1', sha256='a63bc39f301a9adb0b51bae3f2a8c38e06aa380c1eb0012de7ea16872cc22f8d')
    version('0.2.0', sha256='1d5bcded774c4fa960df8b7450f49c320f603fc399bef296fcf5415fa9a3f155')
    version('0.1.0', sha256='16a042def0cd064240df1fbf9dca2dc255f3006d94abbb1a11615a3c98d3a505')


    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('cxxstd',
            default='17',
            values=('17',),
            multi=False,
            description='Use the specified C++ standard when building.')

    variant('ddg4_edm4hep_plugin', default=True,
            description="build the ddg4 plugin for edm4hep output")
    variant('delphes', default=True,
            description="build the delphes plugin for edm4hep output")

    variant('delphes', default=True,
            description="build the delphes plugin for edm4hep output")


    # the cpack configuration fails with an error on some platforms (arch)
    # since it is not used for spack builds, disable
    patch("cpack.patch", when="@0.1.0")

    patch("rootmap.patch", when='@0.1.0')

    depends_on('cmake@3.3:', type='build')
    depends_on('python', type='build')
    depends_on('root@6.08:')
    depends_on('podio@:0.11.0', when='@:0.1.0')
    depends_on('podio@0.12.0:', when='@0.2.0:')


    depends_on('dd4hep@1.12.1: +geant4', when='+ddg4_edm4hep_plugin')
    depends_on("delphes", when="+delphes")
    depends_on("pythia8@:8299", when="@:0.2.0+delphes")

    depends_on('hepmc@:2.99.99', type='test')
    depends_on('heppdt', type='test')
    depends_on('tricktrack@1.0.9:', type='test')


    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(self.define('CMAKE_CXX_STANDARD', self.spec.variants['cxxstd'].value))
        args.append(self.define('BUILD_TESTING', self.run_tests))
        args.append(self.define_from_variant("BUILD_DDG4EDM4HEP", 'ddg4_edm4hep_plugin'))
        args.append(self.define_from_variant("BUILD_DELPHESEDM4HEP", 'delphes'))
        return args


