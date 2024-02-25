# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage
from spack.pkg.k4.key4hep_stack import k4_setup_env_for_framework_tests


class K4clue(CMakePackage, Ilcsoftpackage):
    """CLUE Clustering for Key4hep"""

    url = "https://github.com/key4hep/k4Clue/archive/v01-00-01.tar.gz"
    git = "https://github.com/key4hep/k4Clue.git"
    homepage = "https://github.com/key4hep/k4Clue"

    maintainers = ("vvolkl", "jmcarcell")

    version("main", branch="main")
    version(
        "1.0.5",
        sha256="1c848d72d1f74b057e37c00f6c4d120e5c3b2ba5720b766e5bb09bba8fbf508f",
    )
    version(
        "1.0.4",
        sha256="2b18476ced196f64c2527ed8c68c660e87b4aefbb952de91d2658eb1e352a68a",
    )
    version(
        "1.0.1",
        sha256="bf6c1c626bd21684bca8313525e7f6520bde2b7cd666ecce935209c741d93aec",
    )
    version(
        "1.0", sha256="b1b1c871a2425305e56c1923c31eded300a28cd1a97c55e8b440caaefcafc7d1"
    )

    depends_on("cupla")
    depends_on("alpaka")
    depends_on("k4fwcore")
    depends_on("dd4hep")
    depends_on("py-six", type=("build", "run"))

    # todo: fix type='test'
    depends_on("marlindd4hep")
    depends_on("kaltest")
    depends_on("conformaltracking")
    depends_on("overlay")
    depends_on("marlinreco")
    depends_on("marlintrkprocessors")
    depends_on("ddmarlinpandora")
    depends_on("fcalclusterer")
    depends_on("lctuple")
    depends_on("marlinfastjet")
    depends_on("lcfiplus")
    depends_on("k4marlinwrapper")

    def cmake_args(self):
        args = []
        args.append(self.define("cupla_DIR", self.spec["cupla"].prefix))
        return args

    def setup_run_environment(self, env):
        env.set("K4CLUE", self.prefix.share.k4Clue)
        env.prepend_path("PYTHONPATH", self.prefix.python)
        env.prepend_path("CPATH", self.spec["cupla"].prefix.include)
        env.prepend_path("CPATH", self.spec["alpaka"].prefix.include)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4clue"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["k4clue"].prefix.lib64)

    def setup_build_environment(self, env):
        # k4_setup_env_for_framework_tests(self.spec, env)
        env.prepend_path("CPATH", self.spec["dd4hep"].prefix.include)
        env.prepend_path("CPATH", self.spec["alpaka"].prefix.include)
