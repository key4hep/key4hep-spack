from spack.pkg.k4.key4hep_stack import Key4hepPackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4projecttemplate(CMakePackage, Key4hepPackage):
    """Template for Key4hep framework projects"""

    homepage = "https://github.com/key4hep/k4-project-template/"
    url = (
        "https://github.com/key4hep/k4-project-template/archive/refs/tags/v0.2.0.tar.gz"
    )
    git = "https://github.com/key4hep/k4-project-template.git"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "0.3.0",
        sha256="c0adb1dc9c97bc1b5610727fdaa5e1466d003249a215806e39b605d86ed42537",
    )
    version(
        "0.2.0",
        sha256="213b86a6c1a7c83bcab8bb05e64a35d7f4d206f0c7962c1e51eeb0ee04989c54",
    )

    generator = "Ninja"

    depends_on("ninja", type="build")
    depends_on("edm4hep")
    depends_on("k4fwcore@1.0pre14:", when="@0.3.0:")
    depends_on("k4fwcore@1:")
    depends_on("root")
    depends_on("py-six", type=("build", "run"))

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.set("K4PROJECTTEMPLATE", self.prefix.share.k4ProjectTemplate)

    def setup_build_environment(self, env):
        k4_setup_env_for_framework_tests(self.spec, env)
