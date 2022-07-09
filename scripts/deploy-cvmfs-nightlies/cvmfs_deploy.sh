#!/bin/bash

#Get the line for the CVMFS status and chech if server is transaction
clicdp_status=`cvmfs_server list | grep sw-nightlies`
if [[ $clicdp_status == *"(stratum0 / S3)"* ]]; then
  echo "I am not in transaction"
  # Start transaction
  cvmfs_server transaction sw-nightlies.hsf.org

  # Deploy the nightly build
   ./install_key4hep_nightlies.sh $1

  # Publish changes
  cvmfs_server publish sw-nightlies.hsf.org
  exit 0
else
  (>&2 echo "#################################")
  (>&2 echo "### CVMFS Transaction ongoing ###")
  (>&2 echo "### Nightly deploy cancelled  ###")
  (>&2 echo "#################################")
  exit 1
fi
