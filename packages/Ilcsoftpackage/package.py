# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

def ilc_url_for_version(self, version):
        # translate version numbers to ilcsoft conventions.
        # in spack, the convention is: 0.1 (or 0.1.0) 0.1.1, 0.2, 0.2.1 ...
        # in ilcsoft, releases are dashed and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        base_url = self.url.rsplit('/', 1)[0]
        major = str(version[0]).zfill(2)
        minor = str(version[1]).zfill(2)
        # handle the different cases for the patch version:
        # first case, no patch version is given in spack, i.e 0.1
        if len(version) == 2:
            url = base_url + "/v%s-%s.tar.gz" % (major, minor)
        # a patch version is specified in spack, i.e. 0.1.x ...
        elif len(version) == 3:
            patch = str(version[2]).zfill(2)
            # ... but it is zero, and not part of the ilc release url
            if version[2] == 0:
                url = base_url + "/v%s-%s.tar.gz" % (major, minor)
            # ... if it is non-zero, it is part  of the release url
            else:
                url = base_url + "/v%s-%s-%s.tar.gz" % (major, minor, patch)
        else:
            print('Error - Wrong version format provided')
            return
        return url

class Ilcsoftpackage(Package):
    # needs to be present to allow spack to import this file.
    # the above function could also be a member here, but there is an
    # issue with the logging of packages that use custom base classes.
    pass

