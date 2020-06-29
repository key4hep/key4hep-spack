from spack import *


class Dag(CMakePackage):
    """The DAG tool supports traversal of a Directed Acyclic Graph (also known
    here as DAG)."""

    homepage = "https://github.com/HEP-FCC/dag"
    git = "https://github.com/HEP-FCC/dag.git"
    url      = "https://github.com/HEP-FCC/dag/archive/v0.1.tar.gz"

    maintainers = ['vvolkl']

    version('0.1', '764c915de4ff36f8e195a28d6aa084a6')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')
