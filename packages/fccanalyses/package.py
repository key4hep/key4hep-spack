from spack.pkg.k4.key4hep_stack import Key4hepPackage

class Fccanalyses(CMakePackage, Key4hepPackage):
    """ RDF Analysers for the FCC. """
  
    homepage = 'https://github.com/HEP-FCC/FCCAnalyses'
    git = 'https://github.com/HEP-FCC/FCCAnalyses.git'
    url = 'https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz'

    maintainers = ['vvolkl', 'clementhelsens']
  
    version('master', branch='master')
    version('0.3.3', sha256='04d947517ace952f4bb4b2a9479883b22dce5229084ae4ff037ae299d23e1d2c')
    version('0.3.2', sha256='32a238ebf9019440e81da01e52d3109d32d51c80f7c67a5a456860eb67e42221')
    version('0.3.1', sha256='736e4243493d32744ef5b974ae4e60e43c1ab467ba58df6afdf495fccb165dc3')
    version('0.3.0', sha256='b9ad4f3d9a587f4a1666c9ff5880020f43564a4a0e615d2ce7169bc751134dcf')
    version('0.2.0', sha256='a4a9965751ae489495f8583129f4f0be4e55e8e676a66a08be35181f2395b955')
    
    depends_on("root")
    depends_on("vdt")
    depends_on("fastjet")
    depends_on('python')
    depends_on('edm4hep')
    depends_on('py-awkward')
    depends_on('fcc-edm', when="@:0.2.9")
    depends_on('acts@5.00.0', when="@0.3.0:")
    depends_on('eigen', when="@0.3.0:")

    # todo: update the cmake config to remove this
    def setup_build_environment(self, spack_env):
      spack_env.prepend_path('CPATH', self.spec['vdt'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['edm4hep'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['podio'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['fastjet'].prefix.include)
      if spec.satisfied("@0.3.0:"):
        spack_env.prepend_path('CPATH', self.spec['acts'].prefix.include)
        spack_env.prepend_path('CPATH', self.spec['eigen'].prefix.include)

    def setup_run_environment(self, spack_env):
      spack_env.prepend_path('ROOT_INCLUDE_PATH', self.prefix.include.FCCAnalyses)
      spack_env.prepend_path('PYTHONPATH', self.prefix.python)
      # this should point to share/ by key4hep convention
      #  but we want to make it work with the tutorials
      spack_env.set("FCCANALYSES", self.prefix.python)

    def cmake_args(self):
        return [
            self.define('CMAKE_CXX_STANDARD',
                        self.spec['root'].variants['cxxstd'].value)
        ]
