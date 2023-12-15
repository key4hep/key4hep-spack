#!/bin/bash

# This script sets up the Key4HEP software stack from CVMFS for the nightlies

function usage() {
    echo "Usage: source /cvmfs/sw.hsf.org/key4hep/setup.sh [-r <release>]"
    echo "       -r <release> : setup a specific release, if not specified the latest release will be used"
    echo "       -h           : print this help message"
}

function check_release() {
if [[ "$1" = "-r" && -n "$2" && (! -d "/cvmfs/sw.hsf.org/key4hep/releases/$2" || -z "$(ls "/cvmfs/sw.hsf.org/key4hep/releases/$2" | grep $3)") ]]; then
        echo "Release $2 not found, this is a list of the available releases:"
        find /cvmfs/sw.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*centos7*" |
 \awk -F/ '{print $(NF-1)}' | sort -r
        echo "Aborting..."
        return 1
    fi
    return 0
}

if [[ "$1" = "-h" ]]; then
    usage
    return 0
fi

rel="latest"
if [[ "$1" = "-r" && -n "$2" ]]; then
    rel="$2"
fi

if [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="centos"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = 'VERSION_ID="7"' ]] ||
   [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="rhel"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = VERSION_ID=\"7* ]]; then
    echo "Centos/RHEL 7 detected"
    check_release $1 $2 centos7
    if [ $? -ne 0 ]; then
      return 1
    fi
    k4path="/cvmfs/sw.hsf.org/key4hep/releases/$rel/x86_64-centos7-gcc12.2.0-opt"
elif [[ ("$(cat /etc/os-release | grep -E '^ID=')" = 'ID="almalinux"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = VERSION_ID=\"9*)
    || ("$(cat /etc/os-release | grep -E '^ID=')" = 'ID="rhel"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = VERSION_ID=\"9*) ]]; then
    echo "AlmaLinux/RHEL 9 detected"
    check_release $1 $2 "almalinux9"
    if [ $? -ne 0 ]; then
      return 1
    fi
    k4path="/cvmfs/sw.hsf.org/key4hep/releases/$rel/x86_64-almalinux9-gcc11.3.1-opt"
elif [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID=ubuntu' ]]; then
    echo "Ubuntu detected"
    check_release $1 $2 ubuntu
    if [ $? -ne 0 ]; then
      return 1
    fi
    k4path="/cvmfs/sw.hsf.org/key4hep/releases/$rel/x86_64-ubuntu22.04-gcc11.4.0-opt"
else
    echo "Unsupported OS or OS couldn't be correctly detected, aborting..."
    return 1
fi


setup_script_path=$(ls -t1 $k4path/key4hep-stack/*/setup.sh | head -1)
setup_actual=$(readlink -f $setup_script_path)
export key4hep_stack_version=$(echo "$setup_actual"| grep -Po '(?<=key4hep-stack/)(.*)(?=-[[:alnum:]]{6}/)')

if [ "${rel}" = "latest" ]; then
    echo "Setting up the latest Key4HEP software stack from CVMFS ..."
else
    echo "Setting up the Key4HEP software stack release ${rel} from CVMFS ..."
fi
echo " ...  Key4HEP release: ${key4hep_stack_version}"
echo " ...  Use the following command to reproduce the current environment: "
echo " ... "
echo "         source ${setup_actual}"
echo " ... "
echo " ...  If you have any issues, comments or requests, open an issue at https://github.com/key4hep/key4hep-spack/issues"
source ${setup_actual}
