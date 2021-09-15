# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.key4hep_stack import Key4hepPackage, k4_add_latest_commit_as_version


class Conddbmysql(CMakePackage, Key4hepPackage):
    """ Linear Collider MySQL Conditions Database """

    homepage = "https://github.com/iLCSoft/conddbmysql"
    git      = "https://github.com/iLCSoft/conddbmysql.git"
    url      = "https://github.com/iLCSoft/CondDBMySQL/archive/CondDBMySQL_ILC-0-9-7.tar.gz"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0-9-7', sha256='7cbf9e06e2b3d131939ac0b66816814738e8c5021449f19921b4071c1979ef5a')



    depends_on("mariadb")
    depends_on("ilcutil")



    def cmake_args(self):
        args = []  
        # todo: add variant
        #args.append(self.define('LCCD_CONDDBMYSQL', False))
        return args


