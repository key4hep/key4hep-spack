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

    version('16', '542ce3c064094f2b04456395227621cf')
    version('15', 'f04f7c7495deb84193b49058ea50c111')
    version('14', '1dd287ab24d6c237ccb428cc6dd4a4bf')
    version('13', 'faca7e76269c88099d95ef74525b732f')
    version('12', '450f801f7d60c09bf77cd6013d364c65')
    version('11', '8bcb45a0a38c17d0cf762dadd49d5a02')
    version('10', 'dfc76e38838c15bad29ebc9ebb3d0724')
    version('09', 'ac3ad6211009feaaa58d734101cbc99e')
    version('3.3.3', '1a2099854a4131cd53bd0b90ca0dff3d')
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
