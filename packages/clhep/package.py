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
    list_url = "https://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/"

    version('2.3.2.2', '567b304b0fa017e1e9fbf199f456ebe9')
    version('2.3.1.1', '16efca7641bc118c9d217cc96fe90bf5')
    version('2.3.1.0', 'b084934fc26a4182a08c09c292e19161')
    version('2.3.0.0', 'a00399a2ca867f2be902c22fc71d7e2e')
    version('2.2.0.8', '5a23ed3af785ac100a25f6cb791846af')
    version('2.2.0.5', '1584e8ce6ebf395821aed377df315c7c')
    version('2.2.0.4', '71d2c7c2e39d86a0262e555148de01c1')

    variant('debug', default=False, description="Switch to the debug version of CLHEP.")
    variant('cxx11', default=True, description="Compile using c++11 dialect.")

    depends_on('cmake@2.8.12.2:', when='@2.2.0.4:2.3.0.0')
    depends_on('cmake@3.2:', when='@2.3.0.1:')

    def install(self, spec, prefix):
        # Handle debug
        # Pull out the BUILD_TYPE so we can change it (Release is default)
        cmake_args = [ arg for arg in std_cmake_args if 'BUILD_TYPE' not in arg ]
        build_type = 'Debug' if '+debug' in spec else 'MinSizeRel'
        cmake_args.extend(['-DCMAKE_BUILD_TYPE=' + build_type])

        if '+cxx11' in spec:
            env['CXXFLAGS'] = self.compiler.cxx11_flag
            cmake_args.append('-DCLHEP_BUILD_CXXSTD=' + self.compiler.cxx11_flag)

        # Note that the tar file is unusual in that there's a CLHEP directory (addtional layer)
        cmake_args.append("../CLHEP")

        # Run cmake in a build directory
        with working_dir('build', create=True):
            cmake(*cmake_args)
            make()
            make("install")
