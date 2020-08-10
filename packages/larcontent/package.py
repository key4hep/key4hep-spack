# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Larcontent(CMakePackage):
    """Pandora algorithms and tools for LAr TPC event reconstruction"""

    url      = "https://github.com/PandoraPFA/larcontent/archive/v03-04-00.tar.gz"
    hompage  = "https://github.com/PandoraPFA/larcontent"
    git      = "https://github.com/PandoraPFA/larcontent.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.19.0', sha256='21f52e9d512842e3413967c6b326a8a9fa68e2ac54f39a542c4e31c80dfac3eb')

    patch("path1.patch")
    patch("path2.patch")
    patch("path3.patch")
    patch("path4.patch")

    depends_on("pandorapfa")
    depends_on("pandorasdk")
    depends_on("eigen")

    def cmake_args(self):
        args = [
                '-DCMAKE_MODULE_PATH=%s' % self.spec["pandorapfa"].prefix.cmakemodules,
                "-DCMAKE_CXX_FLAGS=-std=c++17"]
        return args

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        url = base_url + "/v%s_%s_%s.tar.gz" % (major, minor, patch)
        return url

