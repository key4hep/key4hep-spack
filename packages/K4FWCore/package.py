from spack import *

class K4fwcore(CMakePackage):
    """Core framework components of the Key4HEP project"""
    homepage = "https://github.com/key4hep/K4FWCore"
    url = "https://github.com/key4hep/K4FWCore/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/K4FWCore.git"

    version('master', branch='master')
    version('0.1.0', sha256='05326d0f3d222f4a195baebf9c9fc60651621ec293e4384de3aaa81281cbea7a')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('gaudi@32.2:')
    depends_on('root@6.08:')
    depends_on('podio@0.10:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        # Setting this bypasses the get_binary_tag.py script
        # and a check for BINARY_TAG which is not used in this build system
        # should become obsolete with the cmake modernisation in gaudi v34
        if self.spec.satisfies('^gaudi@:34.99'):
          args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

    def url_for_version(self, version):
        # releases are dashes and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/key4hep/K4FWCore/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/key4hep/K4FWCore/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
    
	
