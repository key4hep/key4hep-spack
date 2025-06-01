# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Aprilcontent(CMakePackage, Key4hepPackage):
    """APRIL, Algorithm of Particle Reconstruction for the ILC"""

    url = "https://github.com/SDHCAL/APRILContent"
    homepage = "https://github.com/SDHCAL/APRILContent"
    git = "https://github.com/SDHCAL/APRILContent.git"

    tags = ["hep"]

    maintainers("jmcarcell")

    version("main", branch="current")
    # Use a commit since there is not a recent tag
    version("2024-03-11", commit="5047ff5239438bf4ef7845ca37cad93fc20efdd0")

    depends_on("pandorapfa")
    depends_on("pandorasdk")
    depends_on("root")
    depends_on("mlpack")
    depends_on("armadillo")
    depends_on("boost")

    depends_on("pandoramonitoring", when="+monitoring")

    # With the 2024-03-11 commit, it doesn't build with monitoring disabled
    variant("monitoring", default=True, description="Enable Pandora Monitoring")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            "-DCMAKE_MODULE_PATH=%s" % self.spec["pandorapfa"].prefix.cmakemodules,
            f"-Dmlpack_DIR={self.spec['mlpack'].prefix}",
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define_from_variant("PANDORA_MONITORING", "monitoring"),
        ]
        return args
