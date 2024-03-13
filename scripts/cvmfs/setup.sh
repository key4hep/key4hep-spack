#!/usr/bin/env bash

# This script sets up the Key4hep software stack from CVMFS depending on its
# location it either uses the nightlies or the releases

SCRIPT_SOURCE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)
SCRIPT_BASE_DIR=$(dirname "${SCRIPT_SOURCE}")

function _setup_script_usage() {
     echo "_Setup_Script_Usage: source ${SCRIPT_SOURCE} [-r <release>] [--list-releases [distribution]] [--list-packages [distribution]]"
    echo "       -r <release>, --release <release> : setup a specific release, if not specified the latest release will be used (also used for --list-packages)"
    echo "       -h, --help                        : print this help message"
    echo "       --list-releases [distribution]    : list available releases for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the releases for the detected distribution"
    echo "       --list-packages [distribution]    : list available packages and their versions for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the packages for the detected distribution"
}

function _k4_check_release() {
    local release=${1}
    local os=${2}
    if [[ ! -d "/cvmfs/sw-nightlies.hsf.org/key4hep/releases/${release}" || -z "$(ls "/cvmfs/sw-nightlies.hsf.org/key4hep/releases/${release}" | grep ${os})" ]]; then
        echo "Release ${release} not found, this is a list of the available releases:"
        find /cvmfs/sw-nightlies.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*${os}*" | awk -F/ '{print $(NF-1)}' | sort
        echo "Aborting..."
        return 1
    fi
    return 0
}

function _k4_setup_list_releases() {
    local os=$1
    if [ "$os" = "almalinux" ] || [ "$os" = "almalinux9" ]; then
        name="almalinux9"
    elif [ "$os" = "centos" ] || [ "$os" = "centos7" ]; then
        name="centos7"
    elif [ "$os" = "ubuntu" ] || [ "$os" = "ubuntu22" ]; then
        name="ubuntu22"
    else
        echo "Unsupported OS, aborting..."
        _setup_script_usage
        return 1
    fi
    find ${SCRIPT_BASE_DIR}/releases/ -maxdepth 2 -type d -name "*$name*" |
    \awk -F/ '{print $(NF-1)}' | sort
}

function _k4_setup_list_packages() {
    local os=$1
    if [ "$os" = "almalinux" ] || [ "$os" = "almalinux9" ]; then
        name="almalinux9"
    elif [ "$os" = "centos" ] || [ "$os" = "centos7" ]; then
        name="centos7"
    elif [ "$os" = "ubuntu" ] || [ "$os" = "ubuntu22" ]; then
        name="ubuntu22"
    else
        echo "Unsupported OS, aborting..."
        _setup_script_usage
        return 1
    fi
    find ${SCRIPT_BASE_DIR}/releases/$rel/*$name*/ -maxdepth 2 -mindepth 2 -not -path '*/\.*' -type d | awk -F/ '{if ($NF ~ /develop/) printf "%s develop", $(NF-1); else {split($(NF),arr,"-"); printf "%s ", $(NF-1); printf "%s", arr[1]; for (i=2; i<length(arr); i++) printf "-%s", arr[i] } printf "\n" }'
}

function detect_os() {
    if [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="centos"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="7"' ]] ||
           [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"7* ]]; then
        echo "centos7"
    elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="almalinux"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]] ||
             [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]]; then
        echo "almalinux9"
    elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID=ubuntu' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="22.04"' ]]; then
        echo "ubuntu22.04"
    else
        echo "unknown"
    fi
}

function _k4_setup_print_os_info() {
    local os=${1}
    if [ "$os" = "centos7" ]; then
        echo "Centos/RHEL 7 detected"
        if [ "$rel" = "latest" ]; then
            echo "This OS will reach the end of its maintenance support soon and won't have Key4hep builds in the future, consider upgrading to Alma 9"
        fi
    elif [ "$os" = "almalinux9" ]; then
        echo "AlmaLinux/RHEL 9 detected"
    elif [ "$os" = "ubuntu22.04" ]; then
        echo "Ubuntu 22.04 detected"
    fi
}

os=$(detect_os)
if [ "${os}" = "unknown" ]; then
    echo "Unsupported OS or OS couldn't be correctly detected, aborting..."
    echo "Supported OSes are: CentOS/RHEL 7, AlmaLinux/RHEL 9, Ubuntu 22.04"
    return 1
fi

rel="latest"
while [ $# != 0 ]; do
    case "$1" in
        -h|--help)
            _setup_script_usage
            return 0
            ;;
        --list-*)
            # Either we assume that the user has passed in a dedicated OS or we
            # use the one we discovered
            list_arg="${2:-${os}}"
            shift 2
            ;&
        --list-releases)
            if ! _k4_setup_list_releases "${list_arg}"; then return 1; fi
            return 0
            ;;
        --list-packages)
            if ! _k4_setup_list_packages "${list_arg}"; then return 1; fi
            return 0
            ;;
       -r|--release)
           rel="${2}"
           shift 2
           ;;
       *)
           "Unknown argument ${1}, it will be ignored"
           shift
           ;;
    esac
done

if ! _k4_check_release ${rel} $os; then
    return 1
fi

k4path=$(echo ${SCRIPT_BASE_DIR}/releases/${rel}/*${os}*)

if [ -n "$KEY4HEP_STACK" ]; then
    echo "The Key4hep software stack is already set up, please start a new shell to avoid conflicts"
    return 1
fi

_k4_setup_print_os_info "${os}"

_replace_marlin_dll() {
    # replace the library on MARLIN_DLL with the local one (if any)
    local pkg_name=${1}
    local install_prefix=${2}
    if echo ${MARLIN_DLL} | grep -qE "/${pkg_name}/"; then
        local old_lib=$(echo ${MARLIN_DLL} | tr ":" "\n" | grep -E "/${pkg_name}/")
        local lib_name=$(basename ${old_lib})
        for d in lib lib64; do
            local new_lib=$(pwd)/${install_prefix}/${d}/${lib_name}
            if [ -f ${new_lib} ]; then
                export MARLIN_DLL=$(echo ${MARLIN_DLL%:} | tr ":" "\n" | grep -Ev "/${pkg_name}/" | tr "\n" ":")${new_lib}
                echo "Replaced library on MARLIN_DLL: old: '${old_lib}'"
                echo "                                new: '${new_lib}'"
                break;
            fi
        done
    fi
}

function k4_local_repo() {
    for arg in "$@"; do
        case $arg in
            -h|--help)
                echo "_Setup_Script_Usage: k4_local_repo [install]"
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
    export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PYTHONPATH=$(echo $PYTHONPATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export CMAKE_PREFIX_PATH=$(echo $CMAKE_PREFIX_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PKG_CONFIG_PATH=$(echo $PKG_CONFIG_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export ROOT_INCLUDE_PATH=$(echo $ROOT_INCLUDE_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    _replace_marlin_dll ${current_repo} ${install}
    export PATH=$PWD/$install/bin:$PATH
    export LD_LIBRARY_PATH=$PWD/$install/lib:$PWD/$install/lib64:$LD_LIBRARY_PATH
    export PYTHONPATH=$PWD/$install/python:$PYTHONPATH
    export CMAKE_PREFIX_PATH=$PWD/$install:$CMAKE_PREFIX_PATH
    export PKG_CONFIG_PATH=$PWD/$install/lib/pkgconfig:$PKG_CONFIG_PATH
    export ROOT_INCLUDE_PATH=$PWD/$install/include:$ROOT_INCLUDE_PATH
    if [ "$current_repo" = "k4geo" ]; then
        export K4GEO=$PWD
        echo "Added K4GEO=$PWD"
    fi
    echo "Added $PWD/$install to the environment and removed any paths containing /${current_repo}/"
    echo "Some variables may have to be updated manually to point to the local installation"
}

setup_script_path=$(ls -t1 $k4path/key4hep-stack/*/setup.sh | head -1)
setup_actual=$(readlink -f $setup_script_path)
export key4hep_stack_version=$(echo "$setup_actual"| grep -Po '(?<=key4hep-stack/)(.*)(?=-[[:alnum:]]{6}/)')

if [ "${rel}" = "latest" ]; then
    echo "Setting up the latest Key4hep software stack from CVMFS"
    echo "Note that you are using the latest stack, which may point to a newer stack in the future"
else
    echo "Setting up the Key4hep software stack nightly build ${rel} from CVMFS"
fi
echo "Use the following command to reproduce the current environment: "
echo ""
echo "        source ${setup_actual}"
echo ""
if [[ "${SCRIPT_SOURCE}" =~ "nightlies" ]]; then
    echo "Nightly builds are intended for testing and development, if you need a stable environment use the releases"
fi
echo "If you have any issues, comments or requests, open an issue at https://github.com/key4hep/key4hep-spack/issues"
source ${setup_actual}
