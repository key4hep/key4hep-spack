# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Pandorapfa(Package):
    """Metadata package to bring together and build multiple Pandora libraries.
       NOTE: this recipe is not used to install  other pandora packages, for which
       separate recipes exist. It only installs the cmakemodules directory."""

    url      = "https://github.com/PandoraPFA/PandoraPFA/archive/v03-14-00.tar.gz"
    hompage  = "https://github.com/PandoraPFA/PandoraPFA"
    git      = "https://github.com/PandoraPFA/PandoraPFA.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.14.0', sha256='1490f2504bdbd2960cba35fc552b762e3842d77ed5227f84ddabfde546fe6810')

    patch("path.patch")

    def install(self, a, b):
        install_tree('.', self.prefix)

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

