# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)



class GuineaPig(CMakePackage):
    """Generator of Unwanted Interactions for Numerical Experiment 
    Analysis Program Interfaced to GEANT (C++ version)"""

    homepage = "https://gitlab.cern.ch/clic-software/guinea-pig"
    url      = "https://gitlab.cern.ch/clic-software/guinea-pig/-/archive/v1.2.2rc/guinea-pig-v1.2.2rc.zip"
    git = "https://gitlab.cern.ch/clic-software/guinea-pig.git"

    tags = ['hep']

    version('master', branch='master')
    version('1.2.2rc', 'fec0d1b6aa72523eec4e7c71bca2c1ff', )

    variant('fftw2', default=False, 
        description="Enable Fast Fourier Transform support")
    variant('fftw3', default=True,
        description="Enable Fast Fourier Transfrom support")

    depends_on('fftw@2.0.0:2.9.9', when="+fftw2")
    depends_on('fftw@3.0.0:', when="+fftw3")

    def cmake_args(self):
        args = []

        if '+fftw2' in self.spec:
            args.append('-DFFTW2=ON')

        if '+fftw3' in self.spec:
            args.append("-DFFTW3=ON")
        return args
