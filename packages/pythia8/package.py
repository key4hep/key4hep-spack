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
import os

class Pythia8(Package):
    """Event generator pythia"""

    homepage = "http://home.thep.lu.se/~torbjorn/Pythia.html"
    url      = "http://home.thep.lu.se/~torbjorn/pythia8/pythia8219.tgz"

    version('8219', '3459b52b5da1deae52cbddefa6196feb')
    version('8215', 'b4653133e6ab1782a5a4aa66eda6a54b')
    version('8212', '0886d1b2827d8f0cd2ae69b925045f40')
    version('8210', '685d61f08ca486caa6d5dfa35089e4ab')
    version('8209', '1b9e9dc2f8a2c2db63bce739242fbc12')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('PYTHIA8_DIR', self.prefix)
        spack_env.set('PYTHIA8_XML', os.path.join(self.prefix, "share", "Pythia8", "xmldoc"))
        spack_env.set('PYTHIA8DATA', os.path.join(self.prefix, "share", "Pythia8", "xmldoc"))
