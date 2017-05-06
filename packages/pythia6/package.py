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
#     spack install pythia
#
# You can edit this file again by typing:
#
#     spack edit pythia
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Pythia6(Package):
    """PYTHIA is a program for the generation of high-energy physics events,
    i.e. for the description of collisions at high energies between elementary
    particles such as e+, e-, p and pbar in various combinations."""

    homepage = "https://pythia6.hepforge.org/"
    url      = "http://lcgpackages.web.cern.ch/lcgpackages/tarFiles/spackmirror/pythia6/pythia-6.4.28.tar.gz"

    version('6.4.28', '3cf2b78d08bc6319749e524b3b7b38e3')

    depends_on('cmake')

    def install(self, spec, prefix):
        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path
        cmake_args = [source_directory]

        cmake('-DHEPEVT_SIZE=10000', '-P', 'preparePythia6.cmake')

        cmake_args.extend([
            '-DCMAKE_INSTALL_PREFIX=%s' % prefix
        ])

        cmake_args.extend(std_cmake_args)

        with working_dir(build_directory, create=True):
            cmake(*cmake_args)
            make()
            make("install")
