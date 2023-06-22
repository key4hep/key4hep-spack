from spack.pkg.k4.key4hep_stack import Key4hepPackage 
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class Fccsw(CMakePackage, Key4hepPackage):
    """Software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/FCCSW.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.0pre07', tag="v1.0pre07")
    version('1.0pre06', tag="v1.0pre06")
    version('1.0pre05', tag="v1.0pre05")

    depends_on("gaudi")
    depends_on("k4fwcore")
    depends_on("k4gen")
    depends_on("k4simdelphes")
    depends_on("fccdetectors")
    depends_on("k4simgeant4")
    depends_on("k4reccalorimeter")
    depends_on("lcgeo")
    depends_on("fccanalyses")
    depends_on('root')
    depends_on('py-six', type=('build', 'run'))

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value)
        return args

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("FCCSW", self.prefix.share.FCCSW)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_run_environment(self, env):
        env.set("FCCSW", self.prefix.share.FCCSW)
        env.prepend_path("PYTHONPATH", self.prefix.python)

    def setup_build_environment(self, env):
        self.setup_run_environment(env)
        k4_setup_env_for_framework_tests(self.spec, env)
