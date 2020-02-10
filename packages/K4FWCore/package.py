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
import llnl.util.tty as tty
import subprocess

class K4fwcore(CMakePackage):
    """Core framework components of the Key4HEP project"""
    homepage = "https://github.com/key4hep/K4FWCore"
    git = "https://github.com/key4hep/K4FWCore.git"

    version('master', branch='master')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('lcg', default=True, description="Installed against an LCG Release")
    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')



    depends_on('gaudi')
    depends_on('root')


    depends_on('vdt', when="+lcg")
    depends_on('python', when="+lcg")
    depends_on('davix', when="+lcg")


    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args
    
    def setup_environment(self, spack_env, run_env):
        # Need to explicitly add DD4hep libs to the LD_LIBRARY_PATH since
        # some cmake files (MakeGaudiMap.cmake) only rely on this variable
        #spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['dd4hep'].prefix.lib)

        # Gaudi automatically detects the processor if BINARY_TAG is not defined
        # in the environment. This leads to an error detecting a 'broadwell'
        # platform instead of 'x86_64'. This solves this issue.
        import platform
        binary_tag=["x86_64"]
        tty.msg(platform.linux_distribution()[0])
        if "CentOS" in platform.linux_distribution()[0]:
            binary_tag.append("centos7")
        else:
            binary_tag.append("slc6")

        compiler_labels = {
            "gcc@8.2.0": "gcc8",
            "gcc@8.3.0": "gcc8",
            "gcc@6.2.0": "gcc62"
        }

        binary_tag.append(compiler_labels[str(self.compiler.spec)])
        binary_tag.append("opt")

        spack_env.set('BINARY_TAG', "-".join(binary_tag))
        msg="Defining the following environment variable: BINARY_TAG="+"-".join(binary_tag)
        tty.msg(msg)
	
