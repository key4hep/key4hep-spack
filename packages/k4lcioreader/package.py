from spack.pkg.k4.key4hep_stack import Key4hepPackage

class K4lcioreader(CMakePackage, Key4hepPackage):
    """LCIO reader based on PODIO and EDM4hep"""
    homepage = "https://github.com/key4hep/k4LCIOReader"
    url      = "https://github.com/key4hep/k4LCIOReader/archive/v0.1.0.tar.gz"
    git      = "https://github.com/key4hep/k4LCIOReader.git"

    maintainers = ['mirguest']

    version('master', branch='master')
    version('0.4.2', sha256='2bb8383d95b973676b87b4c8af00fdbd8bb84c2d4e45cacf98490d1946f909b0',
            url='https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.04.02.tar.gz')
    version('0.4.1', sha256='bb93892bb38d4bb3176706f1fc55da8a21742a6fe7d5571914e9cfbc3478a847',
            url='https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.04.01.tar.gz')
    version('0.4.0', sha256='aa1f2bcfabc5b5e3a09cab5408af1402b8a4ddf0927f2f69e62084f568306174')
    version('0.3.2', sha256='7886350cb7598f229bea7d58da602f39d739720f593c254a066bd254cda3a4f5')
    version('0.3.1', sha256='c646673fa4a8acb52a5e7680c7e3918aceee3d20769b921673f8ad951b90926a')
    version('0.3.0', sha256='ce6a5596a21bfa23e641eda84830d8aa7caf15fd47da35878ee61e7f555d0e51')
    version('0.2.0', sha256='346fc2ba4b4175895597e093f566ba6407be9eeb9cde0766304e0f19ad03e081')
    version('0.1.0', sha256='996d1ff78c0a8a2f7f358dd4ea19f955853ad0902ee86b99c484de58c5fc2e2c')

    patch('https://github.com/key4hep/k4LCIOReader/commit/81f4f47ecc7ce904189986e08b949d477c0e4f08.patch',
          sha256='5c88414128ccc9af6b53669f79ac5e4a61c4841d7de5b00a56400c9e92b7d37d',
          when='@0.4.1')


    depends_on('lcio')
    depends_on('podio@0.12:')
    depends_on('edm4hep')
    depends_on('k4fwcore@0.2.0', when='@:0.2.0')
    depends_on('k4fwcore@0.3.0:', when='@0.3:')
    depends_on('root')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
        return args
