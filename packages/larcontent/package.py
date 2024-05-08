# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Larcontent(CMakePackage):
    """Pandora algorithms and tools for LAr TPC event reconstruction"""

    url = "https://github.com/PandoraPFA/larcontent/archive/v03-04-00.tar.gz"
    homepage = "https://github.com/PandoraPFA/larcontent"
    git = "https://github.com/PandoraPFA/larcontent.git"

    tags = ["hep"]

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "4.8.1",
        sha256="b15ffe74cf95f61901ec389ca9c763dc767464fc35c2a6ed800126c2d4d13017",
    )
    version(
        "4.4.0",
        sha256="2a495a3e6c322035c4fa99e66152fc9eb48a516533fd1870a18c889310dbe223",
    )
    version(
        "4.0.0",
        sha256="01a28828a92daa4a95fd7399ec9df3c7be9ac2b33f40c5a031707894a44951cd",
    )
    version(
        "4.0.0",
        sha256="01a28828a92daa4a95fd7399ec9df3c7be9ac2b33f40c5a031707894a44951cd",
    )

    patch("path.patch")

    depends_on("pandorapfa")
    depends_on("pandorasdk")
    depends_on("eigen")

    def cmake_args(self):
        args = [
            "-DCMAKE_MODULE_PATH=%s" % self.spec["pandorapfa"].prefix.cmakemodules,
            "-DCMAKE_CXX_FLAGS=-std=c++17 -Wno-error",
        ]
        return args

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[: self.url.rfind("/")]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        patch = str(version[2]).zfill(2)
        url = base_url + "/v%s_%s_%s.tar.gz" % (major, minor, patch)
        return url
