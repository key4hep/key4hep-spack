# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lccd(CMakePackage, Ilcsoftpackage):
    """Linear Collider Conditions Data toolkit."""

    homepage = "https://github.com/iLCSoft/lccd"
    git = "https://github.com/iLCSoft/lccd.git"
    url = "https://github.com/iLCSoft/lccd/archive/v01-05.tar.gz"

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "1.5.2",
        sha256="0e8929b0f390be112125a1ce12fd9695c7890b5cfef586b56304e4bd08a8ea49",
    )
    version(
        "1.5.1",
        sha256="0566b6d93e489bd6c1c4fe377f7e58dfa84a05de85bcce287505334aef21faef",
    )
    version(
        "1.5.0",
        sha256="876f751bebab760303b8dc3b7c6d4fe7d47ddd5aa19af9338f6565c5b817229b",
    )

    variant("conddbmysql", default=False, description="builds with database support")

    depends_on("ilcutil")
    depends_on("lcio")
    depends_on("lcio@2.20.1:", when="@1.5.2:")
    depends_on("conddbmysql", when="+conddbmysql")

    def cmake_args(self):
        args = []
        # todo: add variant
        args.append(self.define_from_variant("LCCD_CONDDBMYSQL", "conddbmysql"))
        return args
