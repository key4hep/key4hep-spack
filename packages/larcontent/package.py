# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Larcontent(CMakePackage):
    """Pandora algorithms and tools for LAr TPC event reconstruction"""

    url      = "https://github.com/PandoraPFA/larcontent/archive/v03-04-00.tar.gz"
    homepage = "https://github.com/PandoraPFA/larcontent"
    git      = "https://github.com/PandoraPFA/larcontent.git"

    tags = ['hep']

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.24.01', sha256='2cd11a05e87b32af06c27f1fea8d54d67141881b1ae4be72b2068a4f546fde5a')
    version('3.24.00', sha256='02cb1533787f341823763de81478a6cb9be8971fc69be4cb1999f711fbb32f73')
    version('3.23.05', sha256='013c883b174a81dcf1ef3d20171e24c75fb90aace179752969345ad9f0a8eb02')
    version('3.23.04', sha256='0a731a31b84abdaa63a10e1e61e5b6d121a63ba80f67d00edd20e7721cc0bb46')
    version('3.22.11', sha256='4985435c9ca85b6bf5c37be5956fba68c8b3be32b73015118df421496e68e80e')
    version('3.22.9', sha256='44ca286faa93fc77dd78010261f06b85ba512b1135fe6bc40659accb9385104f')
    version('3.19.0', sha256='21f52e9d512842e3413967c6b326a8a9fa68e2ac54f39a542c4e31c80dfac3eb')

    patch("path1.patch")
    patch("path2.patch")
    patch("path3.patch")
    patch("path4.patch")
    patch("range_construct_01.patch")

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

