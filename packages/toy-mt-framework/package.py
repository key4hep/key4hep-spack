from spack import *

class ToyMtFramework(Package):
    homepage = "https://github.com/gartung/toy-mt-framework.git"

    version("dev", git="https://github.com/gartung/toy-mt-framework.git", branch="master")
    depends_on("cmake@3.5:", type='build')
    depends_on("boost@1.60.0")
    depends_on("tbb@20151115oss")

    def install(self, spec, prefix):
            cmake_args = std_cmake_args
            cmake(*cmake_args)
            make()
            make("install")

