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
    fi

    echo ${path}

}
function detect-compiler-version-gcc() {
    local ver=$(gcc --version | grep 'gcc (GCC)' | sed -n 's/gcc (GCC) \([0-9][^ ]*\) *.*/\1/p')
    echo $ver
}

function detect-os() {
    (source /etc/os-release && echo ${ID}${VERSION_ID})
}

##############################################################################
# Generate packages.yaml
##############################################################################
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
    echo "packages:"
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

function yaml-format-package-match-name-in-spack() {
    local pkglcg=$1; shift
    local pkgver=$1; shift
    local pkgpath=$1; shift

    # As Valentin pointed (https://github.com/key4hep/k4-spack/pull/30#issuecomment-688690197),
    # some names in lcg are different from the names in spack, so we need to
    # re-mapping them.

    local pkg=$pkglcg
    local buildable=false

    case $pkg in
        acts_core) pkg=acts;;
        C50)       pkg=c50;;
        CMake)     pkg=cmake;;
        COOL)      pkg=cool;;
        CORAL)     pkg=coral;;
        CouchDB)   pkg=couchdb;;
        CppUnit)   pkg=cppunit;;
        Davix)     pkg=davix;;
        DD4hep)    pkg=dd4hep
                   buildable=true;;
        fftw3)     pkg=fftw;;
        FORM)      pkg=form;;
        Garfield++)pkg=garfield++;;
        Gaudi)     pkg=gaudi;;
        Geant4)    pkg=geant4;;
        GSL)       pkg=gsl;;
        HeapDict)  pkg=heapdict;;
        HepMC)     pkg=hepmc;;
        HepPDT)    pkg=heppdt;;
        herwig++)  pkg=herwig3;;
        java)      pkg=jdk;;
        Jinja2)    pkg=jinja2;;
        LCIO)      pkg=lcio;;
        MarkupSafe)pkg=markupsafe;;
        OWSLib)    pkg=owslib;;
        podio)
                   buildable=true;;
        PyHEADTAIL)pkg=py-pyheadtail;;
        PyJWT)     pkg=py-pyjwt;;
        PyRDF)     pkg=py-pyrdf;;
        QMtest)    pkg=py-qmtest;;
        pythia6)   pkg=pythia6;;
        pythia8)   pkg=pythia8;;
        python)    pkg=python;;
        py*)       pkg=py-${pkg};; # BE CAREFUL: exclude "pythia8", "pythia6", "python", so put them before this line
        R)         pkg=R;;
        recola_SM) pkg=recola_sm;;
        RELAX)     pkg=relax;;
        ROOT)      pkg=root;;
        # FIXME: sherpa-openmpi
        srm-ifce)  pkg=srm_ifce;;
        tbb)       pkg=intel-tbb;;
        Vc)        pkg=vc;;
        VecGeom)   pkg=vecgeom;;
        XercesC)   pkg=xerces-c;;
    esac
        

    echo "  $pkg:"
    echo "    buildable: ${buildable}"
    echo "    paths:"
    echo "      ${pkg}@${pkgver}: ${pkgpath}"
}


function generate-yaml-lcg-packages() {
    yaml-format-package-header
    # using call back to format the packages
    # list-lcg-packages yaml-format-package
    list-lcg-packages yaml-format-package-match-name-in-spack
}

##############################################################################
# Generate compilers.yaml
##############################################################################

function list-compilers() {
    local callbackfn=${1:-echo}; shift

    local osver=$(detect-os)
    local ccver=$(detect-compiler-version-gcc)
    local ccdir=$(detect-compiler-path-gcc)
    ccdir=$(dirname $(dirname $ccdir))

    ${callbackfn} $osver $ccdir $ccver
}

function yaml-format-compiler-header() {
    echo "compilers:"
}

function yaml-format-compiler() {
    local osver=$1; shift
    local ccdir=$1; shift
    local ccver=$1; shift

    echo "- compiler:"
    echo "    environment:"
    echo "      set: {LD_LIBRARY_PATH: ${ccdir}/lib64}"
    echo "    modules: []"
    echo "    operating_system: ${osver}"
    echo "    paths: {cc: ${ccdir}/bin/gcc,"
    echo "      cxx: ${ccdir}/bin/g++,"
    echo "      f77: ${ccdir}/bin/gfortran,"
    echo "      fc: ${ccdir}/bin/gfortran}"
    echo "    spec: gcc@${ccver}"

}

function generate-yaml-compilers() {
    yaml-format-compiler-header
    list-compilers yaml-format-compiler
}


##############################################################################
# Create a spack custom scope config files
##############################################################################

function generate-custom-scope() {

    local pkgyaml=packages.yaml
    local compileryaml=compilers.yaml

    local lcgver=$(lcg-version)
    local lcgarch=$(lcg-arch)

    [ -d "${lcgver}" ] || mkdir ${lcgver} || exit -1
    [ -d "${lcgver}/${lcgarch}" ] || mkdir ${lcgver}/${lcgarch} || exit -1

    pushd ${lcgver}/${lcgarch}

    generate-yaml-lcg-packages > ${pkgyaml}
    generate-yaml-compilers > ${compileryaml}

    popd

}


##############################################################################
# Main
##############################################################################

function main() {
    setup-lcg

    generate-custom-scope
} 

main
