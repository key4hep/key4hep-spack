# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install hep-flare
#
# You can edit this file again by typing:
#
#     spack edit hep-flare
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack.package import *


class Flare(PythonPackage):
    """FLARE: FCCee b2Luigi Automated Reconstruction And Event processing.

    A framework powered by b2luigi to easily run Monte Carlo generators and
    fccanalysis workflows.
    """

    homepage = "https://camcoop1.github.io/FLARE"
    url = "https://pypi.org/project/hep-flare"

    # notify when the package is updated.
    maintainers("CamCoop1", "amanmdesai")

    version("master", branch="main")
    
    version("0.1.9", sha256="67e2fc8aa95f9a05fed964b2c74710c54e97671ce125727c96c4b5e6c370b7dd")
    version("0.1.8", sha256="a7e4b9f3e87a783bbef0279470df8152f267ea7d42d98dcabd0b7383c91efcd9")
    version("0.1.7", sha256="dbb6a3fd93d0635545b5786698ef9fef7456582469869d404f87e038f19ec28b")
    version("0.1.6", sha256="1aa5b25e7d6f3a2f2ca50872577f7d8e0a3927f0b5984cd683f0f36faeb09a57")

    depends_on("b2luigi@1.2.0:", type=("build", "run"))
    depends_on("py-pyyaml@6.0:",     type=("build", "run"))
    depends_on("py-pydantic1",       type=("build", "run"))    

    
