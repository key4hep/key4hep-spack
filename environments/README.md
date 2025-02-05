# Environments

There are several folders with configuration files related to Spack
environments. Some folders may pick up data files that are on cvmfs, and may not
be suitable for every use-case.

## key4hep-base

This is a barebones environment and is the preferred one to use for building or
concretizing the Key4hep stack independently. It will pick up only the
configuration in `key4hep-common`, and is tested in CI to concretize against the
latest tagged version of Spack.

## key4hep-common and key4hep-common-{opt,dbg}

These are configuration folders and contain the common requirements and variants
that are used for the stacks that are on cvmfs. The configuration in
`key4hep-common` is always picked up, and the configuration in
`key4hep-common-{opt,dbg}` is picked up depending on the build type. A python
script is used to make sure the configuration files in one folder don't override
the settings for the same package in another configuration folder.

## key4hep-{nightly,release}-share

These are used to install common files for all nightlies and releases (like the
Geant4 data files), and contain the location of the installed packages on cvmfs
to avoid always reinstalling them.

## key4hep-{nightly,release}-{opt,dbg}

These contain configuration that is different depending on the build type, and
are used for building the Key4hep stack on cvmfs.

## key4hep-nightly-macos

This is an experimental environment to build on MacOS. Builds of the Key4hep
stack on MacOS are not guaranteed to build nor work.

## key4hep-dev-external

This is an environment to build the `key4hep-external-stack`, that contains many
of the dependencies (like ROOT, Geant4, Gaudi, etc.) that are used to build the
Key4hep stack and can be used for other projects.

## contrib-compilers

This is an environment used to install compilers on CVMFS.
