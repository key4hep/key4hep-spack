#!/bin/bash

package_list=$(spack maintainers --by-user vvolkl mirguest tmadlener)

# todo: add packages by hep/key4hep label also?

# prune duplicates (needed if package list is appended to)
#package_list=$(echo ${package_list} | tr ' ' '\n' | sort | uniq | tr '\n' ' ' | sed -e 's/[[:space:]]*$//')

for p in ${package_list}; do
  v=$(spack versions --new $p)
  # ignore pre and rc versions
  v=$(echo $v | sed 's/\S*\(rc\|pre\|alpha\)\S*//g')
  if [[ ! -z "$v" ]]; then
    echo $p: $v >> gh-new-version.log
  fi
done

