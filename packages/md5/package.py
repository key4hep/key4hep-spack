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
#     spack install md5
#
# You can edit this file again by typing:
#
#     spack edit md5
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import sys

class Md5(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://cmsrep.cern.ch/cmssw/cms/SOURCES/slc6_amd64_gcc600/external/md5/1.0.0-giojec/md5.1.0.0-d97a571864a119cd5408d2670d095b4410e926cc.tgz"

    version('1.0.0', 'b154f78e89a70ac1328099d9c3820d13',url='http://cmsrep.cern.ch/cmssw/cms/SOURCES/slc6_amd64_gcc600/external/md5/1.0.0-giojec/md5.1.0.0-d97a571864a119cd5408d2670d095b4410e926cc.tgz')

    # FIXME: Add dependencies if required.

    def install(self, spec, prefix):
        comp=which('gcc')
        cp=which('cp')
        md=which('mkdir')
        md('%s' % prefix.lib)
        md('%s' % prefix.include)      
        if sys.platform == 'darwin': 
          comp('md5.c', '-shared', '-fPIC', '-o', 'libcms-md5.dylib')
          cp('-v','libcms-md5.dylib',prefix.lib)
        else: 
          comp('md5.c', '-shared', '-fPIC', '-o', 'libcms-md5.so')
          cp('-v','libcms-md5.so',prefix.lib)
        cp('-v','md5.h',prefix.include)
