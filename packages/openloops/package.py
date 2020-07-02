# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openloops(SConsPackage):
    """ 	The OpenLoops 2 program is a fully automated implementation
    of the Open Loops algorithm combined with on-the-fly reduction methods,
    which allows for the fast and stable numerical evaluation of tree
    and one-loop matrix elements for any Standard Model process
    at NLO QCD and NLO EW. """

    homepage = "https://openloops.hepforge.org"
    url      = "https://openloops.hepforge.org/downloads?f=OpenLoops-2.1.1.tar.gz"

    maintainers = ['vvolkl']

    #patch('scons_env_fix4.patch')

    version('2.1.1', sha256='f1c47ece812227eab584e2c695fef74423d2f212873f762b8658f728685bcb91')

    depends_on('python', type='build')

    def setup_build_environment(self, env):
      env.set("CC", self.compiler.cc)
      env.set("CXX", self.compiler.cxx)
      env.set("FC", self.compiler.fc)
      env.set("F77", self.compiler.fc)
      env.set("FORTRAN", self.compiler.fc)

    def build_args(self, spec, prefix):
        args = []
        return args
