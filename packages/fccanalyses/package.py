from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage

class Fccanalyses(CMakePackage, Key4hepPackage):
    """ RDF Analysers for the FCC. """
  
    homepage = 'https://github.com/HEP-FCC/FCCAnalyses'
    git = 'https://github.com/HEP-FCC/FCCAnalyses.git'
    url = 'https://github.com/HEP-FCC/FCCAnalyses/archive/v0.1.1.tar.gz'

    maintainers = ['vvolkl', 'clementhelsens']
  
    version('master', branch='master')
    version("0.2.0pre02", tag="v0.2.0pre02")
    
    depends_on("root")
    depends_on("vdt")
    depends_on("fastjet")
    depends_on('python')
    depends_on('edm4hep')
    depends_on('fcc-edm')

    # todo: update the cmake config to remove this
    def setup_build_environment(self, spack_env):
      spack_env.prepend_path('CPATH', self.spec['vdt'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['edm4hep'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['podio'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['fcc-edm'].prefix.include)
      spack_env.prepend_path('CPATH', self.spec['fastjet'].prefix.include)

    def setup_run_environment(self, spack_env):
      spack_env.prepend_path('ROOT_INCLUDE_PATH', self.prefix.include.FCCAnalyses)
