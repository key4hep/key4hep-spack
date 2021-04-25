# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_version


class Generalbrokenlines(CMakePackage):
    """Track refitting with broken lines in 3D."""

    homepage = "https://github.com/GeneralBrokenLines/GeneralBrokenLines"
    url      = "https://github.com/GeneralBrokenLines/GeneralBrokenLines/archive/V02-02-00.tar.gz"
    git      = "https://github.com/GeneralBrokenLines/GeneralBrokenLines.git"

    tags = ['hep']

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('2.2.1', sha256='4200837687c8eb03f7ba719787a2af35691366da258a045f9bb372f8fc69e120')
    version('2.2.0', sha256='81237239415d9c0ee05223c035f22353880084121b587c384ebd0a5754677dfc')
    version('2.1.3', sha256='f96bc7ae5e5d1199517598a44c293b793e5d8e987e1737fae0b67ffc1f8c4f9f')
    version('2.1.2', sha256='a0a81c0682501016df8a0760234138e4546c88dbafa40ef29050d2929bdc9827')
    version('2.1.1', sha256='21fe55d7aee2022a8f7d873c3b191ad334915d643956f18004a6d967d22d3e39')
    version('2.1.0', sha256='27fe33529447b1976ecbdcafaabd1aeab072b5773685a89d6c0f3ac10fd2b920')
    version('2.0.1', sha256='351625b17d51ca6631c7901dcebad80b328def5f05f46b194f1990f547f1e248')
    version('2.0.0', sha256='58ca3e1da1cc198da5bdef9c893c622475fbc145bdd6e2ebcd92e763abcda838')
    version('1.18.0', sha256='1e08bd97bfd6bb4afc165cd960f7e68199085f40bb368163db8885a529c4017e')
    version('1.17.1', sha256='66afdce406f7e7fe06c3faeadd73d651e39b9a2d60d0207b816bc2798159208d')
    version('1.17.0', sha256='f0cd628fd734fc7228ff25bfd20958a7ae4fc2c290796957b3790e617143f56a')

    depends_on('eigen')
    depends_on('root')

    def cmake_args(self):
        args = [ self.define("SUPPORT_ROOT", True) ]
        args.append('-DCMAKE_CXX_STANDARD=%s'
                  % self.spec['root'].variants['cxxstd'].value)

        return args

    def url_for_version(self, version):
        # translate version numbers to ilcsoft conventions.
        # in spack, the convention is: 0.1 (or 0.1.0) 0.1.1, 0.2, 0.2.1 ...
        # in ilcsoft, releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        base_url = self.url.rsplit('/', 1)[0]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        # handle the different cases for the patch version:
        # first case, no patch version is given in spack, i.e 0.1
        if len(version) == 3:
            patch = str(version[2]).zfill(2)
            # ... but it is zero, and not part of the ilc release url
            url = base_url + "/V%s-%s-%s.tar.gz" % (major, minor, patch)
        else:
            print('Error - Wrong version format provided')
            return
        return url

