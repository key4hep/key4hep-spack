
from spack import *


class Edm4hep(CMakePackage):
    """Event data model of Key4HEP"""

    homepage = "https://github.com/key4hep/EDM4hep"
    url = "https://github.com/key4hep/EDM4hep/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/EDM4hep.git"

    version('master', branch='master')
    version('0.1.0', sha256='16a042def0cd064240df1fbf9dca2dc255f3006d94abbb1a11615a3c98d3a505')


    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    _cxx_std_vals = ('14', '17')
    variant('cxxstd',
            default='17',
            values=_cxx_std_vals,
            multi=False,
            description='Use the specified C++ standard when building.')

    variant('ddg4_edm4hep_plugin', default=True,
            description="build the ddg4 plugin for edm4hep output")


    # the cpack configuration fails with an error on some platforms (arch)
    # since it is not used for spack builds, disable
    patch("cpack.patch")

    depends_on('cmake@3.3:', type='build')
    depends_on('python', type='build')

    for s in _cxx_std_vals:
        depends_on('root@6.08: cxxstd=' + s, when='cxxstd=' + s)
        depends_on('podio@0.10.0: cxxstd=' + s, when='cxxstd=' + s)

    depends_on('dd4hep@1.12.1: +geant4', when='+ddg4_edm4hep_plugin')

    depends_on('hepmc@:2.99.99', type='test')
    depends_on('heppdt', type='test')
    depends_on('tricktrack@1.0.9:', type='test')


    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(self.define('CMAKE_CXX_STANDARD', self.spec.variants['cxxstd'].value))
        args.append(self.define('BUILD_TESTING', self.run_tests))
        args.append(self.define_from_variant("BUILD_DDG4EDM4HEP", 'ddg4_edm4hep_plugin'))
        return args


    def url_for_version(self, version):
        # releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/key4hep/edm4hep/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/key4hep/edm4hep/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
