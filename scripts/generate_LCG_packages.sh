#!/bin/bash
# Description:
#   Generate packages.yaml from based on the LCG releases
# Author:
#   Tao Lin <lintao@ihep.ac.cn>

function info:() {
    echo "INFO: $*" 1>&2
}

function error:() {
    echo "ERROR: $*" 1>&2
    exit -1
}

function lcg-view-top-dir() {
    echo /cvmfs/sft.cern.ch/lcg/views
}

function lcg-release-top-dir() {
    echo /cvmfs/sft.cern.ch/lcg/releases
}

function lcg-version() {
    echo LCG_97_FCC_2
}

function lcg-arch() {
    echo x86_64-centos7-gcc8-opt
}

function setup-lcg() {
    local script=$(lcg-view-top-dir)/$(lcg-version)/$(lcg-arch)/setup.sh

    if [ ! -f "$script" ]; then
        error: "Failed to find the setup script: '$script'"
    fi

    source $script
}

function detect-compiler-path-gcc() {
    local path=$(which gcc)

    if [[ $path == $(lcg-release-top-dir)* ]] ; then
        info: "this is a lcg gcc $path"
        echo yes
    else
        echo no
    fi



}
function detect-compiler-version-gcc() {
    local ver=$(gcc --version | grep 'gcc (GCC)' | sed -n 's/gcc (GCC) \([0-9][^ ]*\) *.*/\1/p')
    echo $ver
}

function list-lcg-packages() {
    local callbackfn=${1:-echo}; shift


    local lcgpath=$(lcg-release-top-dir)/$(lcg-version)
    if [ ! -d "$lcgpath" ]; then
        error: "Failed to find LCG $lcgpath"
    fi

    local pkg
    local pkgver
    local pkgpath
    # list all pkgs
    for pkg in $(ls $lcgpath); do
        pkgpath=$lcgpath/$pkg
        if [ ! -d "$pkgpath" ]; then
            continue;
        fi
        # list all versions
        for pkgver in $(ls $pkgpath); do
            pkgpath=$pkgpath/$pkgver
            if [ ! -d "$pkgpath" ]; then
                continue;
            fi

            # then, the arch
            pkgpath=$pkgpath/$(lcg-arch)
            if [ ! -d "$pkgpath" ]; then
                continue;
            fi

            info: "Found $pkg $pkgver $pkgpath"

            # NOW: Format

            ${callbackfn} $pkg $pkgver $pkgpath
            
        done
    done
}

function yaml-format-package-header() {
    echo "packages"
}

function yaml-format-package() {
    local pkg=$1; shift
    local pkgver=$1; shift
    local pkgpath=$1; shift

    echo "  $pkg:"
    echo "    buildable: false"
    echo "    paths:"
    echo "      ${pkg}@${pkgver}: ${pkgpath}"
}

function generate-yaml-lcg-packages() {
    yaml-format-package-header
    # using call back to format the packages
    list-lcg-packages yaml-format-package
}

function main() {
    setup-lcg

    local pkgyaml=packages.yaml

    generate-yaml-lcg-packages > ${pkgyaml}
}

main
