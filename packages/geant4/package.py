from spack import *

class Geant4(Package):
    """Geant4 is a toolkit for the simulation of the passage of particles through matter. Its areas of application include high energy, nuclear and accelerator physics, as well as studies in medical and space science."""

    homepage = "http://geant4.cern.ch/"
    url      = "http://geant4.cern.ch/support/source/geant4.10.01.p03.tar.gz"

    version('10.01.p03', '4fb4175cc0dabcd517443fbdccd97439')

    depends_on("xerces-c")
    depends_on("cmake")

    def install(self, spec, prefix):

        cmake_args = list(std_cmake_args)
        cmake_args.append('-DXERCESC_ROOT_DIR:STRING=%s'%spec['xerces-c'].prefix)
        cmake_args.append('-DGEANT4_BUILD_CXXSTD=c++11')

        cmake_args += ['-DGEANT4_USE_GDML=ON', '-DGEANT4_USE_RAYTRACER_X11=ON']

        # fixme: turn off data for now and maybe each data set should
        # go into a separate package to cut down on disk usage between
        # different code versions using the same data versions.
        cmake_args.append('-DGEANT4_INSTALL_DATA=OFF')

        # http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/InstallationGuide/html/ch02s03.html
        # fixme: likely things that need addressing:
        # -DGEANT4_USE_OPENGL_X11=ON
        # -DGEANT4_USE_SYSTEM_CLHEP
        # -DGEANT4_USE_SYSTEM_EXPAT

        if '+qt' in spec:
            cmake_args.append('-DGEANT4_USE_QT=ON')



        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        with working_dir(build_directory, create=True):
            cmake(source_directory, *cmake_args)
            make()
            make("install")

    def url_for_version(self, version):
         """Handle Geant4's unusual version string."""
         return "http://geant4.cern.ch/support/source/geant4.%s.tar.gz"%version

