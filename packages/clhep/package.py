# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install clhep
#
# You can always get back here to change things with:
#
#     spack edit clhep
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Clhep(Package):
    """CLHEP is a C++ Class Library for High Energy Physics. """
    homepage = "http://proj-clhep.web.cern.ch/proj-clhep/"
    url      = "http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-2.2.0.5.tgz"

    version('2.2.0.5', '1584e8ce6ebf395821aed377df315c7c')
    version('2.3.1.1')

    variant('debug', default=False, description="Switch to the debug version of CLHEP.")
    variant('cxx14', default=True, description="Compile using c++14 dialect.")

    depends_on('cmake @2.8.12.2:')

    def install(self, spec, prefix):

        # Handle debug
        # Pull out the BUILD_TYPE so we can change it (Release is default)
        cmake_args = [ arg for arg in std_cmake_args if 'BUILD_TYPE' not in arg ]
        build_type = 'Debug' if '+debug' in spec else 'MinSizeRel'
        cmake_args.extend(['-DCMAKE_BUILD_TYPE=' + build_type])

        if '+cxx14' in spec:
            env['CXXFLAGS'] = self.compiler.cxx14_flag
            cmake_args.append('-DCLHEP_BUILD_CXXSTD=' + self.compiler.cxx14_flag)

        # Note that the tar file is unusual in that there's a CLHEP directory (addtional layer)
        cmake_args.append("../CLHEP")

        # Run cmake in a build directory
        with working_dir('build', create=True):
            cmake(*cmake_args)
            make()
            make("install")
