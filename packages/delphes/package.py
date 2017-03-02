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


class Delphes(CMakePackage):
    """Event data model description library"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/delphes/delphes"
    url      = "https://github.com/delphes/delphes/archive/3.3.3.tar.gz"

    version('3.3.3', '1a2099854a4131cd53bd0b90ca0dff3d')
    version('3.4.0', 'cfe26bfc2638d195c9880238c6f7adc4')
    version('3.4.1pre01', git=homepage, tag='3.4.1pre01')
    version('develop', git='https://github.com/delphes/delphes.git', branch='master')

    depends_on('cmake', type='build')
    depends_on('root')

    def configure_args(self):
        spec = self.spec
        return [
            '-DCMAKE_BUILD_TYPE:STRING=%s' ('Debug' if '+debug' in spec else 'Release')
        ]

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('DELPHES_DIR', self.prefix)
