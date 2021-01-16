# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 


class K4pandora(CMakePackage, Key4hepPackage):
    """k4Pandora is a pandora app for the Key4HEP software framework"""

    homepage = "https://github.com/key4hep/k4Pandora"
    url      = "https://github.com/key4hep/k4Pandora/archive/master.tar.gz"
    git      = "https://github.com/key4hep/k4Pandora.git"

    maintainers = ['mirguest']

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    k4_add_latest_commit_as_version(git)
    version('master', branch='master')

    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('edm4hep')
    depends_on('k4fwcore@0.3.0:')
    depends_on('gaudi@35.0:')
    depends_on('gear')
    depends_on('lcio')
    depends_on('lccontent')
    depends_on('hepmc')
    depends_on('pandorasdk')
    depends_on('pandorapfa')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
            args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append('-DCMAKE_MODULE_PATH=%s'%cmake_modules)
        return args

