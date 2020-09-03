# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version


class Lcfiplus(CMakePackage):
    """Flavor tagging code for ILC detectors, for documentation consult confluence at https://confluence.slac.stanford.edu/display/ilc/LCFIPlus"""

    url      = "https://github.com/lcfiplus/LCFIPlus/archive/v00-10.tar.gz"
    homepage = "https://github.com/lcfiplus/LCFIPlus"
    git      = "https://github.com/lcfiplus/LCFIPlus.git"

    maintainers = ['vvolkl']

    version('master', branch="master")
    version('0.10',       sha256='0d4d27cd0d9407cd2f13e5a978be8c9389bc86c78c2eefd0ae7c060c4b7196c3')

    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('lcfivertex')
    depends_on('root +tmva')

    patch("dict.patch")

    def cmake_args(self):
        args = []  
        # todo: add variant
        args.append(self.define('INSTALL_DOC', False))
        return args

    @run_after('install')
    def install_source(self):
        install_tree('include', self.prefix.include)

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libLCFIPlus.so")

    def url_for_version(self, version):
        return ilc_url_for_version(self, version)
