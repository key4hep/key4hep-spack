from spack import *

class Fastjet(Package):
    """
    A software package for jet finding in pp and e+e− collisions. It 
    includes fast native implementations of many sequential 
    recombination clustering algorithms, plugins for access to a 
    range of cone jet finders and tools for advanced jet manipulation. 
    """

    homepage = "http://fastjet.fr/"
    url      = "http://fastjet.fr/repo/fastjet-3.1.3.tar.gz"

    version('3.1.3', '30a12aaf5bd53e01d84bd2584f57ddd9')

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)
        make()
        make("install")
