# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage


class Sdhcalcontent(CMakePackage, Key4hepPackage):
    """Plugins for the SDHCAL"""

    url = "https://github.com/SDHCAL/SDHCALContent"
    homepage = "https://github.com/SDHCAL/SDHCALContent"
    git = "https://github.com/SDHCAL/SDHCALContent.git"

    tags = ["hep"]

    maintainers("jmcarcell")

    version("main", branch="main")
    # Use a commit since there is not a recent tag
    version("2024-03-08", commit="c221d1af5c6e587c97ab469a39bf8ed441495c0e")

    depends_on("pandorapfa")
    depends_on("pandorasdk")
    depends_on("root")

    depends_on("pandoramonitoring", when="+monitoring")

    variant("monitoring", default=False, description="Enable Pandora Monitoring")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            "-DCMAKE_MODULE_PATH=%s" % self.spec["pandorapfa"].prefix.cmakemodules,
            f"-DCMAKE_CXX_STANDARD={self.spec['root'].variants['cxxstd'].value}",
            self.define_from_variant("PANDORA_MONITORING", "monitoring"),
        ]
        return args
