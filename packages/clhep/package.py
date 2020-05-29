# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Clhep(CMakePackage):
    """HEP-specific foundation and utility classes such as random generators, physics vectors, geometry and linear algebra"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gitlab.cern.ch/CLHEP/CLHEP"
    git      = "https://gitlab.cern.ch/CLHEP/CLHEP.git"
    url      = "https://gitlab.cern.ch/CLHEP/CLHEP/-/archive/CLHEP_2_4_1_3/CLHEP-CLHEP_2_4_1_3.tar.gz"

    maintainers = ['fdplacido']

    version('2_4_1_3', sha256='aa2725db049c455d8e3c78678889c013deef83bcba0146bdf04e859c38054d52')
    version('2_4_1_2', sha256='bb6e36dc1ab055d0b47bb24377b570b100b37ace402cbc0d858e49be0a1b72c6')
    version('2_4_1_1', sha256='2be516e99bd31c1413a887be4e960dcccd2884754e606bff9a4a048ee3594bbd')
    version('2_4_1_0', sha256='21b6823c8f859f2e042c71032cc23ddcca22a98186a374f0bde4ed54683a649b')
    version('2_4_0_4', sha256='058cf042fedc5ac21c59a4acb2b5af2c56bf4a310456ada4ecf590dd8ac7b444')
    version('2_4_0_3', sha256='0ce6be26d9718e35f7abe60ee8117a4bddebf49a545e506bb0e9c1e72448ce8c')
    version('2_4_0_2', sha256='d459681835ecfa272dfe48d42667f25fb2cb480981c0df381b4c051f26504b80')
    version('2_4_0_1', sha256='1370a036ca8530df97d0c20722f26ace7c34b34070a5d3bf892feeb9d4f83756')
    version('2_4_0_0', sha256='e205c51b7b8e5109d30a55d72570c65440ebf670d43063b729264a4dc69c9645')
    version('2_3_4_6', sha256='ef12c4e0e0452d07f4a5e6370c747589b8bc1ed5001507ccd17685aab4728752')
    version('2_3_4_5', sha256='4ed1b18a0c146a915cbc44b8f6b2b8289c99bf9e9a538bf4db9f7b3bbe3d762e')
    version('2_3_4_4', sha256='f7228b83396ee34e6ab12538c470a3f6bd4d657158dd362bee443a29f1d4abe6')
    version('2_3_4_3', sha256='91eaaaad6c60f58a9bb71ea525259f81829d0f47384a61ca07f8d3920ebb3540')
    version('2_3_4_2', sha256='deaa9396b23779f185eead508fa156637d4c85abfdb3dfb8a673436fa05ad562')
    version('2_3_4_1', sha256='27687bb4e98bac9f2985f92a6fe6c676058abaa96f0ee71451f62f8d76f22bb9')
    version('2_3_4_0', sha256='6cd39e932dcb8b12a50d8dc0a27695662dffb595024ce947b724f4fda4ccba3c')
    version('2_3_3_2', sha256='3dd41587ac99b27c6aa4ca3dd6204ba96b774627f3f28079cf0f01663340a811')
    version('2_3_3_1', sha256='fc837873e4172497f97b8d3e77c7508d6c554320465da73cf6b0bea8a2aae993')
    version('2_3_3_0', sha256='aacf0fdbdd6f38f485533e1b92d383a1eb6252dab8e5644694580cc7121ffe06')
    version('2_3_2_2', sha256='9a9b6ac3e6c6c9dcd29e528a3ac3371a67223c75fb8898770d36d0ae4a222ace')

