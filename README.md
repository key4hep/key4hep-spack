# [Spack](https://github.com/LLNL/spack) package repo for Key4HEP software packaging

This holds a set of Spack packages for common HEP software.  It relies
on Spack and the builtin Spack packages, some of which are overridden
by this repo.

## Getting started

Initial setup like:

```bash
cd /path/to/big/disk
git clone https://github.com/LLNL/spack.git
cd spack/var/spack/repos
git clone https://github.com/key4hep/k4-spack.git
cd -
./spack/bin/spack compiler add /usr/bin/gcc
./spack/bin/spack repo add spack/var/spack/repos/k4-spack
```

To not have to type a full path to `spack` and to gain some other shell-level features do

```bash
$ source spack/share/spack/setup-env.sh
```

This is assumed below.


## Some Exercises

### Install EDM4hep

```bash
$ spack info edm4hep
$ spack install edm4hep
```

### Setup environment

If you have [Environment Modules](http://modules.sf.net) installed:

```bash
$ spack load edm4hep
