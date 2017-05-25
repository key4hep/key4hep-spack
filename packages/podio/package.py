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


class Podio(CMakePackage):
    """Event data model description library"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/HEP-FCC/podio/archive/v0.4.tar.gz"

    version('0.4.1', '6c3e166bfca6a7d36de05cbde3a55713')
    version('0.4'  , '9cb8b0dd4510ed1ee05e03982196151d')
    version('0.3.2', 'ed07d059e0fe79336a8c9c8e8be6d4e1')
    version('0.3.1', 'a7bc95a99af6fc50ae39539e5aa1087e')
    version('0.3'  , '04411e2a48126846f576ca292e4656a0')
    version('develop', git='https://github.com/HEP-FCC/podio.git', branch='master')

    depends_on('cmake', type='build')
    depends_on('py-pyyaml', type='run')
    depends_on('root')

    def configure_args(self):
        spec = self.spec
        return [
            '-DCMAKE_BUILD_TYPE:STRING=%s' ('Debug' if '+debug' in spec else 'Release')
        ]

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('PODIO', self.prefix)
