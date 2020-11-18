# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage, k4_add_latest_commit_as_version

class K4marlinwrapper(CMakePackage, Ilcsoftpackage):
    """Gaudify Marlin Processors in order to run them in the Key4HEP framework"""

    homepage = "https://github.com/key4hep/k4MarlinWrapper"
    git      = "https://github.com/key4hep/k4MarlinWrapper.git"
    url      = "https://github.com/key4hep/k4MarlinWrapper/archive/v00-01.tar.gz"

    maintainers = ['fdplacido']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.2.1', sha256='7aeb0cfff97fe67bb046ea80e7ed219a51c31add2b7770cdb9fd022a1b1497b9')
    version('0.2',    sha256='15809cbc141364c5856c58f8b21e954bde29479703b79020e8b47dbd55f41f73')
    version('0.1',    sha256='d3048178b2f9b721a64ee296019435cbbbce5a65ad956ec733cdb203730db188')


    depends_on('root')
    depends_on('lcio')
    depends_on('marlin')
    depends_on('gaudi@35.0:', when="@0.2.2:")
    depends_on('gaudi@:34.99', when="@:0.2.1")

    def cmake_args(self):
        args = []
        if self.spec.satisfies('^gaudi@:34.99'):
            args += [ self.define('HOST_BINARY_TAG','x86_64-linux-gcc9-opt') ]
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.set("K4MARLINWRAPPER", self.prefix.share.k4MarlinWrapper)
