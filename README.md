# [Spack](https://github.com/spack/spack) package repo for Key4hep software packaging

This repository holds a set of Spack recipes for key4hep software.

Consult the the [key4hep documentation website](https://cern.ch/key4hep) and the
[spack documentation](https://spack.readthedocs.io/en/latest/) for more details.

## Spack Versions
The spack recipes in this repository should work with any recent version of
spack. The nightlies are currently built against the commit of spack that is in
the
[`.latest-commit`](https://github.com/key4hep/key4hep-spack/blob/main/.latest-commit)
file in this repository, which is a tag since Spack v1.0.0. The file
`.latest-packages-commit` contains the commit used for the
[spack-packages](https://github.com/spack/spack-packages) repository. The commit
of spack that was used to build a stack can be found in the file `.spack-commit`
that is shipped with every stack on cvmfs.


## Repository Contents

Apart from the recipes for key4hep packages in the folder `packages`, the
repository contains a collection of environments used to build the stack in
`environments` and some scripts used for publishing on cvmfs and other utilities
in `scripts`. The builds for the Key4hep stack run in Gitlab CI runners and the
workflows can be found in the file `.gitlab-ci.yml` in the [gitlab
repository](https://gitlab.cern.ch/key4hep/k4-deploy).

Additionally, the file `.latest-commit` contains the latest commit of Spack used
for the recent builds, which is updated from time to time to keep up with the
develop branch of Spack. The file `.latest-packages-commit` contains the latest
commit of the[spack-packages](https://github.com/spack/spack-packages)
repository. In addition, the file `.cherry-pick` contains some fixes needed to
build the stack. These can also be found in the file `.cherry-pick` that is
shipped with every stack on cvmfs.

## Central Installations

Installations of the software stack can be found under `/cvmfs/sw.hsf.org` (for
CentOS 7, Ubuntu and Alma 9) and `/cvmfs/sw-nightlies.hsf.org` (AlmaLinux 9 and
Ubuntu 24.04 at the time of writing) see:

https://key4hep.github.io/key4hep-doc/main/getting_started/setup.html

## Requirements

To compile the key4hep stack some system packages are required; without these,
the spack concretization or compilation can fail. The packages needed are an
OpenGL implementation that can be installed with:

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

In addition, for some releases, for Ubuntu and Alma 9 the compilers are picked
up from the system, so, for example, building in an image without `gcc` or
`glibc` won't work. These commands should install most of the compilers and the
development tools:

``` bash
apt install -y build-essential gfortran                            # Ubuntu
dnf groupinstall -y "Development Tools" && dnf install -y gfortran # AlmaLinux 9
```

Dockerfiles with the images that are used to build the key4hep stack can be
found in https://github.com/key4hep/key4hep-images.

## Installing with spack

To install the Key4hep stack with Spack as it is installed for the builds that
are deployed on CVMFS, run the commands:

``` bash

git clone https://github.com/key4hep/key4hep-spack -q
git clone https://github.com/spack/spack -q
cd spack
git checkout $(cat ../key4hep-spack/.latest-commit)
cd ..
source spack/share/spack/setup-env.sh
git clone https://github.com/spack/spack-packages -q
cd spack-packages
git checkout $(cat ../key4hep-spack/.latest-packages-commit)
cd ..

spack repo set --destination "${PWD%/}/spack-packages" builtin
spack repo add key4hep-spack

cd spack-packages
source ../key4hep-spack/.cherry-pick
cd ..

cd key4hep-spack/env/<env_of_your_choice>
spack env activate .

spack concretize
spack install -p 2 # -p 2 for 2 packages being built at the same time
```
