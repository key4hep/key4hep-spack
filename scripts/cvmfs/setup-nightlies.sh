#!/bin/bash
if [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="centos"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = 'VERSION_ID="7"' ]]; then
    echo "Centos 7 detected"
    if [[ "$1" = "-r" && -n "$2" && ! -d "/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$2/x86_64-centos7-gcc12.2.0-opt/key4hep-stack" ]]; then
        echo "Release $2 not found, this is a list of the available releases:"
        find /cvmfs/sw-nightlies.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*centos7*" | \awk -F/ '{print $(NF-1)}' | sort -r
        echo "Aborting..."
        return 1
    fi
    rel="latest"
    if [[ "$1" = "-r" && -n "$2" ]]; then
        rel="$2"
    fi
    k4path="/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$rel/x86_64-centos7-gcc12.2.0-opt"
elif [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="almalinux"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = VERSION_ID=\"9* ]]; then
    echo "AlmaLinux 9 detected"
    if [[ "$1" = "-r" && -n "$2" && ! -d "/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$2/x86_64-almalinux9-gcc11.3.1-opt/key4hep-stack" ]]; then
        echo "Release $2 not found, this is a list of the available releases:"
        find /cvmfs/sw-nightlies.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*almalinux9*" | \awk -F/ '{print $(NF-1)}' | sort -r
        echo "Aborting..."
        return 1
    fi
    rel="latest"
    if [[ "$1" = "-r" && -n "$2" ]]; then
        rel="$2"
    fi
    k4path="/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$rel/x86_64-almalinux9-gcc11.3.1-opt"
elif [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID=ubuntu' ]]; then
    echo "Ubuntu detected"
    if [[ "$1" = "-r" && -n "$2" && ! -d "/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$2/x86_64-ubuntu22.04-gcc11.3.0-opt/key4hep-stack" ]]; then
        echo "Release $2 not found, this is a list of the available releases:"
        find /cvmfs/sw-nightlies.hsf.org/key4hep/releases/ -maxdepth 2 -type d -name "*ubuntu*" | \awk -F/ '{print $(NF-1)}' | sort -r
        echo "Aborting..."
        return 1
    fi
    rel="latest"
    if [[ "$1" = "-r" && -n "$2" ]]; then
        rel="$2"
    fi
    k4path="/cvmfs/sw-nightlies.hsf.org/key4hep/releases/$rel/x86_64-ubuntu22.04-gcc11.3.0-opt"
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
echo " ...  If you have any issues, comments or requests open an issue at https://github.com/key4hep/key4hep-spack/issues"
# source ${setup_actual}

if [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="centos"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = 'VERSION_ID="7"' && ! ("$CPATH" =~ /vdt/) ]]; then
    export CPATH=/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2023-04-25/x86_64-centos7-gcc12.2.0-opt/vdt/0.4.3-3gl6qx/include:$CPATH
elif [[ "$(cat /etc/os-release | grep -E '^ID=')" = 'ID="almalinux"' && "$(cat /etc/os-release | grep -E 'VERSION_ID')" = VERSION_ID=\"9* ]]; then
    export CPATH=/cvmfs/sw-nightlies.hsf.org/key4hep/releases/2023-05-04/x86_64-almalinux9-gcc11.3.1-opt/vdt/0.4.3-w4m63d/include:$CPATH
fi
