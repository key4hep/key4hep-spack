# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Conformaltracking(CMakePackage, Ilcsoftpackage):
    """Package for running pattern recognition based on conformal mapping
       and cellular automaton. This is not tied to a given geometry, but
       has been developed for the CLIC detector model 2015."""

    homepage = "https://github.com/iLCSoft/ConformalTracking/"
    url      = "https://github.com/iLCSoft/ConformalTracking/archive/v01-10.tar.gz"
    git      = "https://github.com/iLCSoft/ConformalTracking.git"


    maintainers = ['vvolkl']

    version('master', branch='master')
    version('1.11',    sha256='297790748e211c7c8e52d70a283d6a9477ea0318db6c8521e640d41e4006520a')
    version('1.10',    sha256='7e0f5774a0ea80147b67db6c218de6001e83e46abc14396564a0a552725dbcce')
    version('1.9',     sha256='c9ae5bd4f833b4542c8e2df01698c1a40ed8bdfc7330eb0e06ec9c3304b2bbca')
    version('1.8',     sha256='e25d2a5df0e77a4223120b0697e2c2414b6ffd12fe6f645c2fbb1a372b635c31')
    version('1.7',     sha256='d16da2af43d2556f870db725c205691b862c90c3d156e202faf2e232153bb3ec')
    version('1.6',     sha256='1efb3df93d22d4b1af6db1d49e91a18ee707b0f1742dd4047cbec3dc408cac31')
    version('1.5',     sha256='4ac891584a719486ef0e8ebf05041b7211a8196b37ad0a27d69a90eb6868d05b')
    version('1.4',     sha256='689e4c87b7c06fcbf7450623f9ecf83cf755e06eb893bf0c69abd3bf17b9f838')
    version('1.3',     sha256='36eae31519ec22d48eb0d148994aaaaa9ef18d5d6fb919a398e680fdc9ccd6c9')
    version('1.2',     sha256='92a1f5af9e3cca25af6b24a7e1fa7210ff4dc09c700315ccb8bb4301ad054427')

    depends_on('ilcutil')
    depends_on('root')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlintrk')
    depends_on('raida')
    depends_on('boost')

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libConformalTracking.so")

    def cmake_args(self):
        # C++ Standard
        return [
            '-DCMAKE_CXX_STANDARD=%s' % self.spec['root'].variants['cxxstd'].value
        ]
