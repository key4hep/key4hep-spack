# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Pandorapfa(Package):
    """Metadata package to bring together and build multiple Pandora libraries.
    NOTE: this recipe is not used to install  other pandora packages, for which
    separate recipes exist. It only installs the cmakemodules directory."""

    url = "https://github.com/PandoraPFA/PandoraPFA/archive/v03-14-00.tar.gz"
    homepage = "https://github.com/PandoraPFA/PandoraPFA"
    git = "https://github.com/PandoraPFA/PandoraPFA.git"

    tags = ["hep"]

    maintainers = ["vvolkl"]

    version("master", branch="master")
    version(
        "4.8.1",
        sha256sum="3b9e224196f09f3ce59062e73e1d05d4e8821d8163025263eee4448f7529f780",
    )
    version(
        "4.4.1",
        sha256="98c628b5063695fa73649136ded0aaa8e40cb34d06000096117606d926599f3b",
    )
    version(
        "4.3.1",
        sha256="2f4757a6ed2e10d3effc300b330f67ba13c499dbf21ba720b29b50527332fcdb",
    )
    version(
        "4.3.0",
        sha256="a794022c33b3a5afc1272740ac385e0c4ab96a112733012e7dfcbe80b5a3b445",
    )
    version(
        "4.2.1",
        sha256="1d262417748d18e00466ae3f1714ab0d7452e903bd1430773a72c652cf4666e4",
    )
    version(
        "4.2.0",
        sha256="5c1030db6047b2d6cef6b534a98f5293e0f97f8e35e92f254f2a61b4a20f5cee",
    )
    version(
        "4.0.0",
        sha256="80fdb60ac53ebada9d6ed2c6d0cefe79174586ce82e2e3bee7eefb4dbacbfba3",
    )

    patch("path.patch")

    def install(self, a, b):
        install_tree("cmakemodules", self.prefix.cmakemodules)

    def url_for_version(self, version):
        # contrary to ilcsoftpackages, here the patch version is kept when 0
        base_url = self.url[: self.url.rfind("/")]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        patch = str(version[2]).zfill(2)
        url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("PANDORAPFA", self.prefix)

    def setup_run_environment(self, env):
        env.set("PANDORAPFA", self.prefix)
