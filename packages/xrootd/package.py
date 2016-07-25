from spack import *

class Xrootd(Package):
    """The XROOTD project aims at giving high performance, scalable fault tolerant access to data repositories of many kinds."""
    homepage = "http://xrootd.org"
    url      = "http://xrootd.org/download/v4.3.0/xrootd-4.3.0.tar.gz"

    version('4.3.0', '39c2fab9f632f35e12ff607ccaf9e16c')

    depends_on('cmake', type='build')

    def install(self, spec, prefix):
        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')

        with working_dir(build_directory, create=True):
            cmake(source_directory, *options)
            make()
            make("install")

