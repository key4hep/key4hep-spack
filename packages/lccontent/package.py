# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Lccontent(CMakePackage):
    """Pandora algorithms and tools for Linear Collider event reconstruction."""

    url      = "https://github.com/PandoraPFA/lccontent/archive/v03-01-05.tar.gz"
    homepage = "https://github.com/PandoraPFA/lccontent"
    git      = "https://github.com/PandoraPFA/lccontent.git"

    tags = ['hep']

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.1.6', sha256='d332c37f5bbc182ac4f90435c2b708152d32c233a1dbc2d71b99b8a5212a1bfa')
    version('3.1.5', sha256='876a49ac79344a55e3bc611dd9668c7c1d90915e66b7fbe0e93c29460d23984b')

    patch("path1.patch")
    patch("path2.patch")
    patch("path3.patch")
    patch("path4.patch")
    patch("bool-int.patch", when="@:3.1.5")

    depends_on("pandorapfa")
    depends_on("pandorasdk")

    def cmake_args(self):
        args = [
                '-DCMAKE_CXX_STANDARD=17',
                '-DCMAKE_MODULE_PATH=%s' % self.spec["pandorapfa"].prefix.cmakemodules
        ]
        if self.spec.satisfies('%clang'):
            args.append('-DCMAKE_CXX_FLAGS=-Wno-error')
        return args

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
