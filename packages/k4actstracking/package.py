
from spack.pkg.k4.key4hep_stack import Key4hepPackage

class K4actstracking(BundlePackage, Key4hepPackage):
    """Acts tracking components for the key4hep project"""

    homepage = "https://github.com/key4hep/k4ActsTracking"
    #todo
    #url = "https://github.com/key4hep/k4ActsTracking"
    git      = "https://github.com/key4hep/k4ActsTracking.git"

    maintainers = ['vvolkl']

    version('main', branch='main')

    depends_on('acts+dd4hep+tgeo+identification')
