# [Spack](https://github.com/spack/spack) package repo for Key4HEP software packaging

This repository holds a set of Spack recipes for key4hep software.

Consult the [spack documentation](https://spack.readthedocs.io/en/latest/) and
the [key4hep documentation website](https://cern.ch/key4hep) for more details.

## Spack Versions
The spack recipes in this repository should work with any version of spack (0.19
is known to work and it's possible older versions work too, newer than 0.19
works). Some of the environments require spack 0.20 or newer since they use (or
they include a file that uses) the `require` keyword which was introduced in
[spack 0.20](https://github.com/spack/spack/releases/tag/v0.20.0).

### Repository Contents

Apart from the recipes for key4hep packages in the folder `packages`, the
repository contains a collection of environments used to build the stack in
`environments` and some scripts used for publishing on cvmfs and other utilities in
`scripts`.

### Central Installations

Installations of the software stack can be found under `/cvmfs/sw.hsf.org` (for
CentOS 7) and `/cvmfs/sw-nightlies.hsf.org` (for CentOS 7, AlmaLinux 9 and
Ubuntu) see:

https://key4hep.github.io/key4hep-doc/setup-and-getting-started/README.html
