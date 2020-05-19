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
source spack/share/spack/setup-env.sh
```

This is assumed below.


## Some Exercises

### Install EDM4hep

```bash
spack info edm4hep
spack install edm4hep
```

### Setup environment

If you have [Environment Modules](http://modules.sf.net) installed:

```bash
spack load edm4hep
```

### Working around spack concretizer problems

Currently the default settings for some of the packages here do not work due to
known [short comings of the spack
concretizer](https://spack.readthedocs.io/en/latest/known_issues.html#variants-are-not-properly-forwarded-to-dependencies).
For example `spack install K4FWCore` will most probably fail with the following error

```
1. "cxxstd=11" conflicts with "root+root7" [root7 requires at least C++14]
```

Instead of fixing all the packages to deal with these issues, one of the
following workarounds can be used. The issues in spack are planned to be fixed
with the next spack release which would hopefully make these obsolete.

#### Requiring a specific package version

The simplest solution to the above problem is to simply require a `root` version
with the appropriate requirements, e.g.

```bash
spack install K4FWCore ^root cxxstd=17
```

will tell spack to use `cxxstd=17` also for building `root` and get rid of the
conflict above. If using this, make sure to use the same value for `cxxstd` for
`K4FWCore` and `root`.

#### Requiring certain variants globally

spack can be configured using some [configuration
files](https://spack.readthedocs.io/en/latest/configuration.html). Specifically
using `packages.yaml` which is read from the user directory, i.e. `~/.spack` (or
`/.spack/linux`) can be used to enforce he value of certain default variants
globally. To solve the above problem it is enough to put the following into
`packages.yaml`:

```yaml
packages:
  all:
  variants: cxxstd=17
  ```

It is still possible to override this for certain packages either by
individually configuring them in `packages.yaml` or via the command line which
take precedence over all configuration files.
