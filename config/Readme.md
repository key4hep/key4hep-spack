This directory contains config files for spack. `packages.yaml` sets some more optimal variants and the build target microarchitecture, and `cvmfs_build/config.yaml` controls the directory structure for builds intended for cvmfs.

Another file `compilers.yaml` is typically needed by spack, but contains paths to the compiler, which may differ on different build machines. The best way to create this one is to set up the desired compiler and run `spack compiler find`
