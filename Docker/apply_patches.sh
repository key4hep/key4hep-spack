#!/bin/bash

# Get file to patch
if [ ${#} != 1 ]; then
    echo "usage: ${0} /path/to/repo"
    exit 1
fi

REPO=${1}

# Determine what commit of spack we have
cd ${SPACK_ROOT}
SPACK_COMMIT=$(git rev-parse HEAD)

# Determine key4hep supported spack commit
SPACK_COMMIT_REPO=$(cat ${REPO}/.latest-commit)

if [ "${SPACK_COMMIT}" != "${SPACK_COMMIT_REPO}" ]; then
    echo "Spack version not officially tested."
    echo " recommended version: ${SPACK_COMMIT_REPO}"
    echo " our version: ${SPACK_COMMIT}"
    echo "Ignoring patches..."
    exit 0
fi

# Apply the patches to spack
echo "Applying patches from ${REPO}..."
cd ${SPACK_ROOT}
source ${REPO}/.cherry-pick
