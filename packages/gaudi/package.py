from spack import *

class Gaudi(Package):
    """Gaudi framework."""
    homepage = "https://gaudi.cern.ch"
    url      = "http://gaudi.cern.ch"

    version('v27r1', '7d7283ca2c3d8d050af3db2b89a25ab629abbb57')

    depends_on("python")
    depends_on("root")
    depends_on("py-qmtest")
    depends_on("clhep")
    depends_on("boost@1.59.0")
    depends_on("cppunit")
    depends_on("aida")

    def install(self, spec, prefix):
        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug ')

	#options.append("-DCMAKE_TOOLCHAIN_FILE=" + source_directory +"/toolchain.cmake")

        with working_dir(build_directory, create=True):
            import os
            cmake(source_directory , *options)
            make()
            make("install")

    def url_for_version(self, version):
        """Handle ROOT's unusual version string."""
        #return "http://lhcbproject.web.cern.ch/lhcbproject/dist/GAUDI/GAUDI_GAUDI_%s.tar.gz" % version
        return "http://cern.ch/bcouturi/Gaudi_%s.tar.gz" % version
