#!/usr/bin/env bash

_replace_marlin_dll() {
    # replace the library on MARLIN_DLL with the local one (if any)
    local pkg_name=${1}
    local install_prefix=${2}
    if echo ${MARLIN_DLL} | grep -qE "/${pkg_name}/"; then
        local old_lib=$(echo ${MARLIN_DLL} | tr ":" "\n" | grep -E "/${pkg_name}/")
        local lib_name=$(basename ${old_lib})
        local new_lib=$(pwd)/${install_prefix}/lib/${lib_name}
        export MARLIN_DLL=$(echo ${MARLIN_DLL%:} | tr ":" "\n" | grep -Ev "/${pkg_name}/" | tr "\n" ":")${new_lib}
        echo "Replaced library on MARLIN_DLL: old: '${old_lib}'"
        echo "                                new: '${new_lib}'"
    fi
}

k4_local_repo() {
    for arg in "$@"; do
        case $arg in
            -h|--help)
                echo "Usage: k4_local_repo [install]"
                echo "       install : the directory where the software is installed (default: ./install)"
                echo "       -h      : print this help message"
                echo "Run the function from the directory where the repository is located."
                return 0
                ;;
            *)
                ;;
        esac
    done

    if [ -n "$1" ]; then
        install=$1
    else
        install=install
    fi
    current_repo=$(basename $PWD | tr '[:upper:]' '[:lower:]' | tr -d -)
    export PATH=$(echo $PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export ROOT_LIBRARY_PATH=$(echo $ROOT_LIBRARY_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PYTHONPATH=$(echo $PYTHONPATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export CMAKE_PREFIX_PATH=$(echo $CMAKE_PREFIX_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PKG_CONFIG_PATH=$(echo $PKG_CONFIG_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export ROOT_INCLUDE_PATH=$(echo $ROOT_INCLUDE_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    _replace_marlin_dll ${current_repo} ${install}
    export PATH=$PWD/$install/bin:$PATH
    export ROOT_LIBRARY_PATH=$PWD/$install/lib:$PWD/$install/lib64:$ROOT_LIBRARY_PATH
    export LD_LIBRARY_PATH=$PWD/$install/lib:$PWD/$install/lib64:$LD_LIBRARY_PATH
    # Get the python site-packages directory
    libpythondir=$(python -c "import site; print('/'.join(site.getsitepackages()[0].split('/')[-3:]))")
    export PYTHONPATH=$PWD/$install/python:$PWD/$install/$libpythondir:$PYTHONPATH
    export PYTHONPATH=$PWD/$install/python:$PYTHONPATH
    export CMAKE_PREFIX_PATH=$PWD/$install:$CMAKE_PREFIX_PATH
    export PKG_CONFIG_PATH=$PWD/$install/lib/pkgconfig:$PKG_CONFIG_PATH
    export ROOT_INCLUDE_PATH=$PWD/$install/include:$ROOT_INCLUDE_PATH
    if [ "$current_repo" = "k4geo" ]; then
        export LCGEO=$PWD
        export K4GEO=$PWD
        export lcgeo_DIR=$PWD
        export k4geo_DIR=$PWD
        echo "Added LCGEO, K4GEO, lcgeo_DIR and k4geo_DIR to the environment"
    fi
    echo "Added $PWD/$install to the environment and removed any paths containing /${current_repo}/"
    echo "Some variables may have to be updated manually to point to the local installation"
}


