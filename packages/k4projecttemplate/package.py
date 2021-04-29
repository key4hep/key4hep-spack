
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage

class K4projecttemplate(CMakePackage, Key4hepPackage):
    """Template for Key4hep framework projects"""
    homepage = "https://github.com/key4hep/k4-project-template/"
    url      = "https://github.com/key4hep/k4-project-template/archive/refs/tags/v0.2.0.tar.gz"
    git      = "https://github.com/key4hep/k4-project-template.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.2.0', sha256='213b86a6c1a7c83bcab8bb05e64a35d7f4d206f0c7962c1e51eeb0ee04989c54')


    generator = 'Ninja'

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17', '20'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('ninja', type='build')
    depends_on("edm4hep")
    depends_on('k4fwcore@1:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.set("K4PROJECTTEMPLATE", self.prefix.share.k4ProjectTemplate)
