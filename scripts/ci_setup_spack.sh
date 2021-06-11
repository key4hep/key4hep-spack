# set up spack inside the k4-spack repo
 if [ -n "$SPACK_VERSION" ]; then git clone  https://github.com/key4hep/spack ; cd spack; git checkout $SPACK_VERSION; cd ..; else git clone --depth 1 https://github.com/key4hep/spack; fi 
 source spack/share/spack/setup-env.sh
 mkdir spack/var/spack/repos/key4hep-spack
 cp -r * spack/var/spack/repos/key4hep-spack || true
# clean up git directories for zip
 rm -rf spack/var/spack/repos/key4hep-spack/spack || true
 rm -rf spack/.git
# register k4 package recipes with spack
 echo "repos:" > spack/etc/spack/repos.yaml
 echo ' - $SPACK_ROOT/var/spack/repos/key4hep-spack' >> spack/etc/spack/repos.yaml
# get the right config files to the right places
 cp ${PWD}/spack/var/spack/repos/key4hep-spack/config/cvmfs_build/upstreams.yaml spack/etc/spack/
 cp ${PWD}/spack/var/spack/repos/key4hep-spack/environments/key4hep-common/packages.yaml spack/etc/spack/
 cp ${PWD}/spack/var/spack/repos/key4hep-spack/environments/key4hep-common/compilers.yaml spack/etc/spack/
 tar -czf key4hep-spack_centos7-cvmfs.tar.gz spack
# remove the config files again 
 rm spack/etc/spack/upstreams.yaml
 rm spack/etc/spack/compilers.yaml
 rm spack/etc/spack/packages.yaml
 tar -czf key4hep-spack.tar.gz spack
