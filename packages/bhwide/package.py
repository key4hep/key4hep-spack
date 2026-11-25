# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

import os


class Bhwide(MakefilePackage):
    """BHWIDE is the state of art Monte Carlo for Bhabha generation at FCC-ee."""

    bhwide_version = "1.08"
    homepage = "https://placzek.web.cern.ch/bhwide/"
    url = f"https://github.com/KrakowHEPSoft/BHWIDE/archive/refs/tags/v{bhwide_version}.tar.gz"
    git = "https://github.com/KrakowHEPSoft/BHWIDE.git"

    tags = ["hep"]

    version(
        bhwide_version,
        sha256="91fa616091fd38a77eb0bf0f96b60e0e1d0ca15dd6d160099fbeaf61a061cb95",
    )

    patch(f"bhwide-{bhwide_version}-minimal.patch", level=0)

    depends_on("fortran", type="build")

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        chmod = which("chmod")

        mkdirp(prefix.bin)

        install(join_path("bin", "bhwide"), join_path(prefix.bin, "BHWIDE.exe"))
        chmod("755", join_path(prefix.bin, "BHWIDE.exe"))

        script_sh = join_path(os.path.dirname(__file__), "BHWIDE")
        script = prefix.bin.BHWIDE
        install(script_sh, script)
        chmod("755", script)
