##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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


class Tricktrack(CMakePackage):
    """TrickTrack aims to encapsulate the Cellular-Automaton based seeding code
    used in CMSSW in a standalone library."""

    homepage = "https://cern.ch/tricktrack"
    url      = "https://github.com/HEP-SF/TrickTrack/archive/v1.0.4.tar.gz"

    version('1.0.5', '65493aa89361c139c28f63b473459312')
    version('1.0.4', '7fefd2f94c4925d307897b483b9eb039')
    version('1.0.1', 'ec23cadf8b7fa4a343e513c7c988e27f')
    version('0.1',   'a75c6e2c7d7df5b713aa087827503e3c')

    depends_on('eigen', when="@1.0.4:")

    patch('eigen.patch', when="@1.0.4")
    patch('findeigen.patch', when="@1.0.4")
