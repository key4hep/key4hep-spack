from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage

class Fccanalyses(CMakePackage, Key4hepPackage):
    """ RDF Analysers for the FCC. """
  
    homepage = 'https://github.com/HEP-FCC/FCCAnalyses'
    git = 'https://github.com/HEP-FCC/FCCAnalyses.git'
    url = 'https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz'

    maintainers = ['vvolkl', 'clementhelsens']
  
    version('master', branch='master')
    version('0.3.0', sha256='b9ad4f3d9a587f4a1666c9ff5880020f43564a4a0e615d2ce7169bc751134dcf')
    version('0.2.0',      sha256='a4a9965751ae489495f8583129f4f0be4e55e8e676a66a08be35181f2395b955')
    
    depends_on("root")
    depends_on("vdt")
    depends_on("fastjet")
    depends_on('python')
    depends_on('edm4hep')
    depends_on('fcc-edm', when="@:0.2.9")
    depends_on('acts', when="@0.3.0:")

    # todo: update the cmake config to remove this
    def setup_build_environment(self, spack_env):
      spack_env.prepend_path('CPATH', self.spec['vdt'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['edm4hep'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['podio'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['fcc-edm'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['fastjet'].prefix.include)

    def setup_run_environment(self, spack_env):
      spack_env.prepend_path('ROOT_INCLUDE_PATH', self.prefix.include.FCCAnalyses)
      spack_env.prepend_path('PYTHONPATH', self.prefix.python)
      spack_env.set_path("FCCANALYSES", self.prefix.share.FCCAnalyses)
