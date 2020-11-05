
class Fccanalyses(BundlePackage):
  """ Analysis for the FCC. This package is usually built locally, but could be installed with spack (todo). """

  homepage = 'https://github.com/HEP-FCC/FCCAnalyses'

  version('main')

  depends_on('py-particle')
  depends_on('py-awkward1')
  depends_on('py-matplotlib')
  depends_on('py-uproot4')
  #depends_on('py-tensorflow') # todo: check if we should integrate.
  #depends_on('py-zfit') # todo: add in spack
