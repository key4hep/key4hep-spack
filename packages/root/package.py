from spack import *

class Root(Package):
    """ROOT is a data analysis framework."""
    homepage = "https://root.cern.ch"
    url      = "https://root.cern.ch/download/root_v6.07.02.source.tar.gz"

    version('6.07.02', '3fb585bf9fa6ce06ca503173c8bee107')

    depends_on("pcre")
    depends_on("fftw")
    depends_on("graphviz")
    depends_on("python")
    depends_on("gsl")
    depends_on("libxml2")
    depends_on("libpng")
    depends_on("jpeg")
    depends_on("openssl")
    depends_on("freetype")

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

    def url_for_version(sefl, version):
        """Handle ROOT's unusual version string."""
        return "https://root.cern.ch/download/root_v%s.source.tar.gz" % version
