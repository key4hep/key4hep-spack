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
    homepage = "https://github.com/PandoraPFA/PandoraPFA"
    git      = "https://github.com/PandoraPFA/PandoraPFA.git"

    tags = ['hep']

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('3.21.01', sha256='36dd20235d924b975c167a450943d5f70c9e76d95eea0f55c68b0eead6c99e47')
    version('3.21.00', sha256='c36070916691bd4137a6a21aced2efd730cfe31a17819cf94511351b6edfec8d')
    version('3.20.05', sha256='dae829821dbc4d662818f5593e9899b482878c993c4fdebcd6e7bfd4b6e0a9fe')
    version('3.20.04', sha256='6ccec85d1c89e75a941dafd75fccba7ef205f44a79508d9deeca03337cd084aa')
    version('3.20.03', sha256='3a7609f12f6da279e6dbef07986aa7128f4bd9876c80eaa44a1af089694c1f43')
    version('3.20.02', sha256='f1afcd204890a0a5c26b192d36428581770d5855ee54db51b69b7a2c5ac0b944')
    version('3.20.01', sha256='bd8862de38b972d27a802f1e69fee000fe8dd14e85fa10709ce9f897122ade13')
    version('3.20.00', sha256='510998cb984fdbcb38b46711bef475df44dd04c5d72a083c4d28b1d5757e0539')
    version('3.19.12', sha256='a908a93fbfada1faea605aad49082d5fd8b4c4d387658975313fb1441a15ae55')
    version('3.19.11', sha256='c426324ca0be497619185ee066e62758d071672ce5402350bfe40eff91c9565d')
    version('3.19.9', sha256='96e68f455989d523343cdd0513019c9cd9486bcc417962e80b6ffcc7daa3b78d')
    version('3.14.0', sha256='1490f2504bdbd2960cba35fc552b762e3842d77ed5227f84ddabfde546fe6810')

    patch("path.patch")

    def install(self, a, b):
        install_tree('cmakemodules', self.prefix.cmakemodules)

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[:self.url.rfind("/")]
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set('PANDORAPFA', self.prefix)

    def setup_run_environment(self, env):
        env.set('PANDORAPFA', self.prefix)

