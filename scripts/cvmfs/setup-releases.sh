#!/bin/bash

# This script sets up the Key4hep software stack from CVMFS for the nightlies

function usage() {
    echo "Usage: source /cvmfs/sw.hsf.org/key4hep/setup.sh [-r <release>] [--list-releases [distribution]] [--list-packages [distribution]]"
    echo "       -r <release> : setup a specific release, if not specified the latest release will be used (also used for --list-packages)"
    echo "       -h           : print this help message"
    echo "       --list-releases [distribution] : list available releases for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the releases for the detected distribution"
    echo "       --list-packages [distribution] : list available packages and their versions for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the packages for the detected distribution"
}

function check_release() {
if [[ "$1" = "-r" && -n "$2" && (! -d "/cvmfs/sw.hsf.org/key4hep/releases/$2" || -z "$(ls "/cvmfs/sw.hsf.org/key4hep/releases/$2" | grep $3)") ]]; then
        echo "Release $2 not found, this is a list of the available releases:"
        find /cvmfs/sw.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*$3*" |
 \awk -F/ '{print $(NF-1)}' | sort
        echo "Aborting..."
        return 1
    fi
    return 0
}

function list_release() {
    os=$1
    if [ "$os" = "almalinux" ] || [ "$os" = "almalinux9" ]; then
        name="almalinux9"
    elif [ "$os" = "centos" ] || [ "$os" = "centos7" ]; then
        name="centos7"
    elif [ "$os" = "ubuntu" ] || [ "$os" = "ubuntu22" ]; then
        name="ubuntu22"
    else
        echo "Unsupported OS, aborting..."
        usage
        return 1
    fi
    find /cvmfs/sw.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*$name*" |
    \awk -F/ '{print $(NF-1)}' | sort
}

function list_packages() {
    local os=$1
    if [ "$os" = "almalinux" ] || [ "$os" = "almalinux9" ]; then
        name="almalinux9"
    elif [ "$os" = "centos" ] || [ "$os" = "centos7" ]; then
        name="centos7"
    elif [ "$os" = "ubuntu" ] || [ "$os" = "ubuntu22" ]; then
        name="ubuntu22"
    else
        echo "Unsupported OS, aborting..."
        usage
        return 1
    fi
    find /cvmfs/sw.hsf.org/key4hep/releases/$rel/*$name*/ -maxdepth 2 -mindepth 2 -not -path '*/\.*' -type d | awk -F/ '{if ($NF ~ /develop/) printf "%s develop", $(NF-1); else {split($(NF),arr,"-"); printf "%s ", $(NF-1); printf "%s", arr[1]; for (i=2; i<length(arr); i++) printf "-%s", arr[i] } printf "\n" }'
}


rel="latest"
if [[ "$1" = "-r" && -n "$2" ]]; then
    rel="$2"
fi

if [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="centos"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="7"' ]] ||
   [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"7* ]]; then
    os="centos7"
    k4path=$(echo /cvmfs/sw.hsf.org/key4hep/releases/$rel/*centos7*)
elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="almalinux"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]] ||
     [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]]; then
    os="almalinux9"
    k4path=$(echo /cvmfs/sw.hsf.org/key4hep/releases/$rel/*almalinux9*)
elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID=ubuntu' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="22.04"' ]]; then
    os="ubuntu22.04"
    k4path=$(echo /cvmfs/sw.hsf.org/key4hep/releases/$rel/*ubuntu22*)
else
    echo "Unsupported OS or OS couldn't be correctly detected, aborting..."
    echo "Supported OSes are: CentOS/RHEL 7, AlmaLinux/RHEL 9, Ubuntu 22.04"
    return 1
fi

check_release $1 $2 $os
if [ $? -ne 0 ]; then
  return 1
fi

for ((i=1; i<=$#; i++)); do
    eval arg=\$$i
    case $arg in
        -h|--help)
            usage
            return 0
            ;;
        *)
            ;;
    esac
done

for ((i=1; i<=$#; i++)); do
    eval arg=\$$i
    eval "argn=\${$((i+1))}"
    case $arg in
        --list-releases)
            if [ ! -n "$argn" ]; then
                list_release $os
                return 0
            elif [ -n "$argn" ] && [[ "$argn" =~ ^(almalinux|centos|ubuntu) ]]; then
                list_release $argn
                return 0
            else
                echo "Unsupported OS $argn, aborting..."
                usage
                return 1
            fi
            ;;
        --list-packages)
            if [ ! -n "$argn" ]; then
                list_packages $os
                return 0
            elif [ -n "$argn" ] && [[ "$argn" =~ ^(almalinux|centos|ubuntu) ]]; then
                list_packages $argn
                return 0
            else
                echo "Unsupported OS $argn, aborting..."
                usage
                return 1
            fi
            ;;
        -r)
            ;;
        *)
            eval "prev=\${$((i-1))}"
            if [ "$prev" != "-r" ]; then
                echo "Unknown argument $arg, aborting..."
                usage
                return 1
            fi
            ;;
    esac
done

if [ -n "$KEY4HEP_STACK" ]; then
    echo "The Key4hep software stack is already set up, please start a new shell to avoid conflicts"
    return 1
fi

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
    export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PYTHONPATH=$(echo $PYTHONPATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export CMAKE_PREFIX_PATH=$(echo $CMAKE_PREFIX_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PKG_CONFIG_PATH=$(echo $PKG_CONFIG_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export ROOT_INCLUDE_PATH=$(echo $ROOT_INCLUDE_PATH | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export MARLIN_DLL=$(echo $MARLIN_DLL | tr ":" "\n" | grep -Ev "/${current_repo}/" | tr "\n" ":")
    export PATH=$PWD/$install/bin:$PATH
    export LD_LIBRARY_PATH=$PWD/$install/lib:$PWD/$install/lib64:$LD_LIBRARY_PATH
    export PYTHONPATH=$PWD/$install/python:$PYTHONPATH
    export CMAKE_PREFIX_PATH=$PWD/$install:$CMAKE_PREFIX_PATH
    export PKG_CONFIG_PATH=$PWD/$install/lib/pkgconfig:$PKG_CONFIG_PATH
    export ROOT_INCLUDE_PATH=$PWD/$install/include:$ROOT_INCLUDE_PATH
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
    echo "Setting up the Key4hep software stack release ${rel} from CVMFS"
fi
echo "Use the following command to reproduce the current environment: "
echo ""
echo "        source ${setup_actual}"
echo ""
echo "Nightly builds are intended for testing and development, if you need a stable environment use the releases"
echo "If you have any issues, comments or requests, open an issue at https://github.com/key4hep/key4hep-spack/issues"
source ${setup_actual}
