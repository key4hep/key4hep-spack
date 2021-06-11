#!/bin/bash

package_list=$(spack maintainers --by-user vvolkl mirguest tmadlener)

# todo: add packages by hep/key4hep label also?

# prune duplicates (needed if package list is appended to)
#package_list=$(echo ${package_list} | tr ' ' '\n' | sort | uniq | tr '\n' ' ' | sed -e 's/[[:space:]]*$//')

for p in ${package_list}; do
  # ignore deprecated packages
  if [[ "$p" == "py-awkward1" ]] || [[ "$p" == "py-uproot4" ]]; then
    continue
  fi
  v=$(spack versions --new $p)
  # ignore pre and rc versions (for all packages)
  v=$(echo $v | sed 's/\S*\(rc\|pre\|alpha\)\S*//g')
  # ignore alpha and beta versions for py-kubernetes
  if [[ "$p" == "py-kubernetes" ]] ; then
    v=$(echo $v | sed 's/\S*\(a\|b\)\S*//g')
  fi
  # ignore version 00-03-02 for edm4hep which has no code changes
  if [[ "$p" == "edm4hep" ]] ; then
    v=$(echo $v | sed 's/\S*\(00-03-02\)\S*//g')
  fi
  # using `echo $v` instead of "$v" will handle v=" " correctly
  if [[ ! -z `echo $v` ]]; then
    echo "- [ ] \`$p\`: \`$v\` " >> gh-new-version.log
  fi
done

