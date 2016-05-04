from spack import *
import sys

class Root(Package):
    """ROOT is a data analysis framework."""
    homepage = "https://root.cern.ch"
    url      = "https://root.cern.ch/download/root_v6.07.02.source.tar.gz"

    version('6.07.02', '3fb585bf9fa6ce06ca503173c8bee107')
    version('6.06.02', 'e9b8b86838f65b0a78d8d02c66c2ec55')

    if sys.platform == 'darwin': patch('math_uint.patch')

    variant('graphviz', default=False, description='Enable graphviz support')

    depends_on("cmake")
    depends_on("pcre")
    depends_on("fftw")
    depends_on("graphviz",when="+graphviz")    
    depends_on("python")
    depends_on("gsl")
    depends_on("libxml2+python")
    depends_on("jpeg")
    depends_on("openssl@1.0.2f")
    depends_on("freetype")
    if sys.platform != 'darwin': 
        depends_on("libpng")

    def install(self, spec, prefix):


        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        options=[source_directory]
        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')
        else:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Release')
        
        options.extend(std_cmake_args)

        if sys.platform == 'darwin': 
            darwin_options= [
            '-Dcastor=OFF',
            '-Drfio=OFF',
            '-Dbonjour=OFF',
            '-Dcocoa=OFF',
            '-Dx11=ON',
            '-Ddcache=OFF' ]
            options.extend(darwin_options)

        def setup_dependent_environment(self, module, spec, dep_spec):
           """Root wants to set ROOTSYS"""
           os.environ['ROOTSYS'] = self.prefix
 

        with working_dir(build_directory, create=True):
            cmake(*options)
            make()
            make("install")

    def url_for_version(self, version):
        """Handle ROOT's unusual version string."""
        return "https://root.cern.ch/download/root_v%s.source.tar.gz" % version
