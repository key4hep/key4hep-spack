
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class Fccsw(CMakePackage, Key4hepPackage):
    """Software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/FCCSW.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.0pre05', tag="v1.0pre05")

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on("gaudi", type=("test", "run"))
    depends_on("k4fwcore", type=("test", "run"))
    depends_on("k4gen", type=("test", "run"))
    depends_on("k4simdelphes", type=("test", "run"))
    depends_on("fccdetectors", type=("test", "run"))
    depends_on("k4simgeant4", type=("test", "run"))
    depends_on("k4reccalorimeter", type=("test", "run"))
    depends_on("fcc-edm", type=("test", "run"))
    depends_on("lcgeo", type=("test", "run"))

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.set("FCCSW", self.prefix.share.FCCSW)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_run_environment(self, spack_env):
        spack_env.set("FCCSW", self.prefix.share.FCCSW)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_build_environment(self, spack_env):
        spack_env.set("FCCSW", self.prefix.share.FCCSW)
        spack_env.prepend_path("PYTHONPATH", self.prefix.python)
