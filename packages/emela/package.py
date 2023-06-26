# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

class Emela(CMakePackage):
    """Library that implements the evolution in pure QED of the unpolarised electron parton distribution functions (PDFs) up to next-to-leading logarithmic (NLL) approximation"""

    homepage = "https://github.com/jmcarcell/eMELA"
    url = "https://github.com/gstagnit/eMELA/archive/refs/tags/v1.0.tar.gz"

    maintainers = ["jmcarcell"]

    version(
        "1.0",
        sha256="53a867616f7ae0b03928c5a9db4b1b04a6b29794c9492a96b19dfea64b1c856d",
    )

    variant("lhapdf", default=True, description="Use LHAPDF")
    variant("shared", default=False, description="Build libraries as shared instead of static")

    depends_on("boost")
    depends_on("lhapdf", when="+lhapdf")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_LHAPDF", "lhapdf"),
            self.define_from_variant("SHARED", "shared"),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
