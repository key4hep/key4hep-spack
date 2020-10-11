# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cepcsw
#
# You can edit this file again by typing:
#
#     spack edit cepcsw
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cepcsw(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/cepc/CEPCSW"
    url      = "https://github.com/cepc/CEPCSW/archive/master.zip"
    git      = "https://github.com/cepc/CEPCSW.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['mirguest']


    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    # FIXME: Add proper versions here.
    # version('1.2.4')
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('edm4hep')
    depends_on('k4fwcore')
    depends_on('gaudi')
    depends_on('gear')
    depends_on('lcio')
    depends_on('lccontent')
    depends_on('pandorasdk')
    depends_on('pandorapfa')
    depends_on('podio')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
            args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')

        clhep_prefix = self.spec["clhep"].prefix
        clhep_include = clhep_prefix + "/include"
        args.append('-DCLHEP_INCLUDE_DIR=%s'%clhep_include)

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append('-DCMAKE_MODULE_PATH=%s'%cmake_modules)
        return args
