##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Edm4hep(CMakePackage):
    """Event data model of Key4HEP"""

    homepage = "https://github.com/HSF/EDM4hep"
    git = "https://github.com/HSF/EDM4hep.git"

    version('develop', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake', type='build')
    depends_on('python', type='build')
    depends_on('root')
    depends_on('podio@develop')
    depends_on('tbb', when="+lcg")
    depends_on('davix', when="+lcg")

    # in LCG_96 ROOT is installed with an external xz rather than the builtin,
    # so the genreflex binary needs to find it.
    # As root is installed as an external package we cannot modify its
    # setup_dependent_environment function to add the xz lib folder to the
    # LD_LIBRARY_PATH hence we need to do it here.
    depends_on('xz', when='^root@6.16:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    # Override pre-defined test step
    # Multiple tests access to the same root file, thus we avoid parallel
    # execution at this stage
    def check(self):
        with working_dir(self.build_directory):
            make("test", "CTEST_OUTPUT_ON_FAIL=1")

    def setup_environment(self, spack_env, run_env):
	# needed for genreflex
    	spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
    	run_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
        if 'xz' in self.spec:
            spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['xz'].prefix.lib)

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        #spack_env.set('EDM4hep', self.prefix)
        pass
