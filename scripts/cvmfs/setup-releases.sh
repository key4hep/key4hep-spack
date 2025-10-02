#!/bin/bash

# This script sets up the Key4hep software stack from CVMFS for the stable releases

function usage() {
    echo "Usage: source /cvmfs/sw.hsf.org/key4hep/setup.sh [-r <release>] [--list-releases [distribution]] [--list-packages [distribution]]"
    echo "       -d           : setup the debug version of the software stack"
    echo "       -r <release> : setup a specific release, if not specified the latest release will be used (also used for --list-packages)"
    echo "       --help, -h   : print this help message"
    echo "       --list-releases [distribution] : list available releases for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the releases for the detected distribution"
    echo "       --list-packages [distribution] : list available packages and their versions for the specified distribution (almalinux, centos, ubuntu). By default (no OS is specified) it will list the packages for the detected distribution"
    echo "In addition, after sourcing, the command k4_local_repo can be used to add the current repository to the environment"
    echo "It will delete all the existing paths containing the repository name and add some predefined paths to the environment"
}

function check_release() {
if [[ "$1" = "-r" && -n "$2" && (! -d "/cvmfs/sw.hsf.org/key4hep/releases/$2" || -z "$(/usr/bin/ls "/cvmfs/sw.hsf.org/key4hep/releases/$2" | grep $3)") ]]; then
        echo "Release $2 with build type $build_type not found, this is a list of the available releases:"
        list_releases $3
        echo "Aborting..."
        return 1
    fi
    return 0
}

function list_releases() {
    if [ ! -n "$1" ]; then
        os=$os
    else
        os=$1
    fi
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
    find /cvmfs/sw.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*$name*$compiler*$build_type*" |
    \awk -F/ '{print $(NF-1)}' | sort
    unset compiler
}

function list_packages() {
    if [ ! -n "$1" ]; then
        os=$os
    else
        os=$1
    fi
    if [ "$os" = "almalinux" ] || [ "$os" = "almalinux9" ]; then
        name="almalinux9"
    elif [ "$os" = "ubuntu" ] || [ "$os" = "ubuntu22" ]; then
        name="ubuntu22"
    else
        echo "Unsupported OS, aborting..."
        usage
        return 1
    fi

    previous_scratch_releases=()
    while IFS= read -r line; do
        previous_scratch_releases+=("$line")
    done < <(find /cvmfs/sw.hsf.org/key4hep/releases/ -maxdepth 3 -mindepth 3 -type f -name ".scratch" | grep "$name" | grep opt | sort | xargs -n1 dirname)
    for release in "${previous_scratch_releases[@]}"; do
        # Get the latest previous or equal date
        if [[ "$(basename $(dirname $release))" = "$rel" ]] || [[ "$(basename $(dirname $release))" < "$rel" ]]; then
            latest_previous_release=$release
        fi

    done

    # Define an array containing the paths to the folders
    folders=("$latest_previous_release")
    if [ "$build_type" = "dbg" ] && [ -d $(echo $latest_previous_release | sed 's/opt/dbg/') ]; then
        folders+=($(echo $latest_previous_release | sed 's/opt/dbg/'))
    fi
    folders+=(/cvmfs/sw.hsf.org/key4hep/releases/$rel/*$name*-*$build_type*)

    declare -A package_versions

    for folder in "${folders[@]}"; do
        for package in $(ls $folder); do
            package_name=$(basename "$package")
            version_string=$(ls $folder/$package_name -t | head -n 1)
            package_version=$(echo "$version_string" | awk '{if ($NF ~ /develop/) {split($NF,arr,"_"); printf "%s", arr[1]} else {split($(NF),arr,"-"); printf "%s", arr[1]; for (i=2; i<length(arr); i++) printf "-%s", arr[i] } printf "\n" }')
            package_versions["$package_name"]="$package_version"
        done
    done

    # Print the final version for each package
    if [ -z "$ZSH_VERSION" ]; then
        # Bash
        for package_name in $(printf "%s\n" "${!package_versions[@]}" | sort); do
            package_version="${package_versions[$package_name]}"
            echo "$package_name $package_version"
        done
    else
        # Zsh
        for key in ${(ok)package_versions}; do
            echo "$key $package_versions[$key]" | tr -d '"'
        done
    fi

    unset compiler
}


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

build_type=opt
for ((i=1; i<=$#; i++)); do
    eval arg=\$$i
    eval "argn=\${$((i+1))}"
    case $arg in
        -d)
            build_type=dbg
            ;;
        -h|--help)
            usage
            return 0
            ;;
    esac
done


rel="latest-$build_type"
if [[ "$1" = "-r" && -n "$2" ]]; then
    rel="$2"
fi

# Build types are supported only after 2024-10-03
if [[ ! "$rel" == "latest"* ]] && [[ "$rel" < "2024-10-03" ]]; then
    build_type=""
fi

if [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="centos"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="7"' ]] ||
   [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"7* ]]; then
    os="centos7"
elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="almalinux"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]] ||
     [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rhel"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9* ]] ||
     [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID="rocky"' && "$(grep -E 'VERSION_ID' /etc/os-release)" = VERSION_ID=\"9*  ]]; then
    os="almalinux9"
elif [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID=ubuntu' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="22.04"' ]] ||
     [[ "$(grep -E '^ID=' /etc/os-release)" = 'ID=pop' && "$(grep -E 'VERSION_ID' /etc/os-release)" = 'VERSION_ID="22.04"' ]]; then
    os="ubuntu22"
else
    echo "Unsupported OS or OS couldn't be correctly detected, aborting..."
    echo "Supported OSes are: CentOS/RHEL 7, AlmaLinux/RockyLinux/RHEL 9, Ubuntu 22.04"
    return 1
fi

check_release $1 $2 $os
if [ $? -ne 0 ]; then
  return 1
fi

for ((i=1; i<=$#; i++)); do
    eval arg=\$$i
    eval "argn=\${$((i+1))}"
    case $arg in
        --help|-h)
            usage
            return 0
            ;;
        --list-releases)
            if [ ! -n "$argn" ]; then
                list_releases $os
                return 0
            elif [ -n "$argn" ] && [[ "$argn" =~ ^(almalinux|centos|ubuntu) ]]; then
                list_releases $argn
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
        -d)
            ;;
        -r)
            ;;
        *)
            eval "prev=\${$((i-1))}"
            if [ "$prev" != "-r" ]; then
                echo "Unknown argument $arg, it will be ignored"
                # usage
                # return 1
            fi
            ;;
    esac
done

k4path=$(/usr/bin/ls -rd /cvmfs/sw.hsf.org/key4hep/releases/$rel/*$os*$compiler*$build_type | head -n1)

if [ -n "$KEY4HEP_STACK" ]; then
    echo "The Key4hep software stack is already set up, please start a new shell to avoid conflicts"
    return 1
fi

if [ "$os" = "centos7" ]; then
    echo "Centos/RHEL 7 detected"
    if [ "$rel" = "latest" ]; then
        echo "This OS has reached the end of its maintenance support and won't have Key4hep builds in the future, consider upgrading to Alma 9"
    fi
elif [ "$os" = "almalinux9" ]; then
    echo "AlmaLinux/RockyLinux/RHEL 9 detected"
elif [ "$os" = "ubuntu22.04" ]; then
    echo "Ubuntu 22.04 detected"
fi


setup_script_path=$(/usr/bin/ls -t1 $k4path/key4hep-stack/*/setup.sh | head -1)
setup_actual=$(readlink -f $setup_script_path)
export key4hep_stack_version=$(echo "$setup_actual"| grep -Po '(?<=key4hep-stack/)(.*)(?=-[[:alnum:]]{6}/)')

# For SWAN
if [ -n "$LCG_VERSION" ]; then
    echo "A LCG stack has been sourced, unsetting the following variables to avoid conflicts:"
    echo "CMAKE_PREFIX_PATH CPPYY_BACKEND_LIBRARY LD_LIBRARY_PATH PKG_CONFIG_PATH PYTHONHOME PYTHONPATH"
    unset CMAKE_PREFIX_PATH CPPYY_BACKEND_LIBRARY LD_LIBRARY_PATH PKG_CONFIG_PATH PYTHONHOME PYTHONPATH
fi

if [ "${rel}" = "latest" ]; then
    echo "Setting up the latest Key4hep software stack from CVMFS"
    echo "Note that you are using the latest stack, which may point to a newer stack in the future"
else
    echo "Setting up the Key4hep software stack release ${rel} from CVMFS"
fi
command="source /cvmfs/sw.hsf.org/key4hep/setup.sh -r $(basename $(dirname $(dirname $(dirname $(dirname $setup_actual)))))"
if [ "$build_type" = "dbg" ]; then
    command+=" -d"
fi
echo "Use the following command to reproduce the current environment: "
echo ""
echo "        $command"
echo ""
echo "If you have any issues, comments or requests, open an issue at https://github.com/key4hep/key4hep-spack/issues"
source ${setup_actual}
echo "Tip: A new -d flag can be used to access debug builds, otherwise the default is the optimized build"
