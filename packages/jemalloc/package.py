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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install jemalloc
#
# You can edit this file again by typing:
#
#     spack edit jemalloc
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Jemalloc(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.canonware.com/download/jemalloc/jemalloc-4.2.0.tar.bz2"

    version('4.2.1', '094b0a7b8c77c464d0dc8f0643fd3901')
    version('4.2.0', 'e6b5d5a1ea93a04207528d274efdd144')
    version('4.1.1', '7184512da1e4d3331f9587036a6c4739')
    version('4.1.0', 'c4e53c947905a533d5899e5cc3da1f94')
    version('4.0.4', '687c5cc53b9a7ab711ccd680351ff988')



    def install(self, spec, prefix):
        filter_file(r"'-no-cpp-precomp'", "", 'configure',
            string=True)
        # FIXME: Modify the configure line to suit your build system here.
        configure('--prefix={0}'.format(prefix), '--disable-stats')

        # FIXME: Add logic to build and install here.
        make()
        make('install')
