from spack import *
from spack.package import PackageBase

class Key4hepStack(PackageBase):
    """Dummy package to install the Key4hep software development environment."""

    phases = ['build', 'install']
    build_system_class = 'BundlePackage'

    url = 'https://github.com/citibeth/dummy/tarball/v1.0'

    version('1.0', 'e2b724dfcc31d735897971db91be89ff')

    depends_on('cmake', type='build')
    depends_on('podio')
    depends_on('edm4hep')
    depends_on('K4fwcore')


    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        pass
