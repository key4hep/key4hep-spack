from spack import *

class Lcgcmake(Package):
    """Description"""

    homepage = "https://gitlab.cern.ch/sft/lcgcmake"
    url      = "https://gitlab.cern.ch/sft/lcgcmake.git"

    version('84', git='https://gitlab.cern.ch/sft/lcgcmake.git', branch='LCG_84')

    depends_on('cmake')
    depends_on('python')

    def install(self, spec, prefix):
        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        options.append('-DLCG_VERSION=%s' % self.version)

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')

        with working_dir(build_directory, create=True):
            cmake(source_directory, *options)
            make()
            make("install")

