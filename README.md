# [Spack](https://github.com/spack/spack) package repo for Key4HEP software packaging

This repository holds a set of Spack recipes for key4hep software.

Consult the the [key4hep documentation website](https://cern.ch/key4hep) and the
[spack documentation](https://spack.readthedocs.io/en/latest/) for more details.

## Spack Versions
The spack recipes in this repository should work with any version of spack (0.19
is known to work and it's possible older versions work too, newer than 0.19
works). Some of the environments require spack 0.20 or newer since they use (or
they include a file that uses) the `require` keyword which was introduced in
[spack 0.20](https://github.com/spack/spack/releases/tag/v0.20.0).

## Repository Contents

Apart from the recipes for key4hep packages in the folder `packages`, the
repository contains a collection of environments used to build the stack in
`environments` and some scripts used for publishing on cvmfs and other utilities
in `scripts`. The builds run in Gitlab CI runners and the workflows can be found
in the file `.gitlab-ci.yml` in the [gitlab
repository](https://gitlab.cern.ch/key4hep/k4-deploy).

Additionally, the file `.latest-commit` contains the latest commit of Spack used
for the recent builds, which is updated from time to time to keep up with the
develop branch of Spack.

## Central Installations

Installations of the software stack can be found under `/cvmfs/sw.hsf.org` (for
CentOS 7) and `/cvmfs/sw-nightlies.hsf.org` (for CentOS 7, AlmaLinux 9 and
Ubuntu) see:

https://key4hep.github.io/key4hep-doc/setup-and-getting-started/README.html

## Requirements

To compile the key4hep stack some package systems are required; without these,
the spack concretization or compilation can fail. The packages needed are an
OpenGL implementation that can be installed:

``` bash
yum install -y mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel      # Centos 7
apt install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa libglu1-mesa-dev  # Ubuntu 
dnf install -y mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel      # AlmaLinux 9
```

The environments that make use of these libraries or headers expect them to be
found under `/usr`, which is the typical location when they are installed
system-wide (for example in `/usr/include` or `/usr/lib`).

Alternatively, one can install
[HEP_OSlibs](https://gitlab.cern.ch/linuxsupport/rpms/HEP_OSlibs), which will
install the previous and more libraries.
