from spack import *
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_version


class Tricktrack(CMakePackage):
    """TrickTrack aims to encapsulate the Cellular-Automaton based seeding code
    used in CMSSW in a standalone library."""

    homepage = "https://cern.ch/tricktrack"
    url      = "https://github.com/HSF/TrickTrack/archive/v1.0.8.tar.gz"
    git      = "https://github.com/HSF/TrickTrack.git"

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('1.0.9', sha256='988cedbb28ec8f5cc95b762aa8a38e36d75cfc47bd009c9dc4ef365e9751b80d')
    version('1.0.8', sha256='fe5f8d178f8a0a28ac423ad6e9c449772ba547ec3ef7e365c4644d9b5b44cf85')
    version('1.0.7', sha256='e567de7c3c6e8096bd77873ac59fc4667661cdb380d089dcd6443a9d9834f3ef')
    version('1.0.6', sha256='c7c5d6c492f65acd020a600664c5fa75c5caf9de33bb392f46771abad7650398')
    version('1.0.5', sha256='5fe3f9ac523ca2381b11aef57057ec75b85aa9ee0a3fb6bac4710d2c76961692')
    version('1.0.4', sha256='de4b1245a94e0905bcb9387e4a3b675298de916e631d3136f32ac1ab9e01855d')
    version('1.0.1', sha256='4b7fbd3734a5ef30a3abecaf7b15318a1856ff31fac822775035e00669dc921d')

    variant('documentation',     default=False, 
            description='Build doxygen documentation')
    variant('python',            default=False, 
            description='Build python bindings')
    variant('logger',            default=False, 
            description='Use spdlog for logging')
    variant('logger_standalone', default=False, 
            description='Use spdlog standalone (as opposed to in a framework)')

    depends_on('eigen', when="@1.0.4:")

    depends_on('doxygen', when="+documentation")
    depends_on('spdlog', when="+logger")
    depends_on('python', when="+python", type=('run'))

    patch('eigen.patch', when="@1.0.4")
    patch('findeigen.patch', when="@1.0.4")

    def cmake_args(self):
      spec = self.spec

      args = [
              '-Dtricktrack_documentation:BOOL=%s' % (
              'ON' if '+documentation' in spec else 'OFF'),
              '-Dtricktrack_python:BOOL=%s' % (
              'ON' if '+python' in spec else 'OFF'),
              ]

      if '+logger' in spec:
        args.extend(['-DUSE_SPDLOG'])
      if '+logger_standalone' in spec:
        args.extend(['-DUSE_SPDLOG_STANDALONE'])
      return args
