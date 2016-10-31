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
#     spack install vdt
#
# You can edit this file again by typing:
#
#     spack edit vdt
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Vdt(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/dpiparo/vdt/archive/v0.3.2.tar.gz"

    version('0.3.7', 'd2621d4c489894fd1fe8e056d9a0a67c')
    version('0.3.6', '6eaff3bbbd5175332ccbd66cd71a741d')
    version('0.3.5', '399c60c73f0d0acdbfe8eb3fad9061fe')
    version('0.3.4', 'cb7c117e00b80f154cc9c6c7da57c949')
    version('0.3.3', '8fb755df3f8fdf0858603ca1af790d61')
    version('0.3.2', '0d4571b8ced1b97bc13580dab8ccf41d')
    version('0.3.1', '413f411a8b7a9653d1c52371476f2115')

    # FIXME: Add additional dependencies if required.
    depends_on('cmake', type='build')

    def install(self, spec, prefix):
        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path
        options=['-DCMAKE_INSTALL_PREFIX=%s' % self.prefix]
        options.append('-DPRELOAD:BOOL=ON')
        options.append('-DSSE:BOOL=ON')
        options.append('-DNEON:BOOL=OFF')
        options.append(source_directory)

        with working_dir(source_directory):
            # FIXME: Modify the cmake line to suit your build system here.
            cmake(*options)

            # FIXME: Add logic to build and install here.
            make('VERBOSE=1')
            make('install', 'VERBOSE=1')
