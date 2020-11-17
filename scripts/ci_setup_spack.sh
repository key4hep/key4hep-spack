# set up spack inside the k4-spack repo
 if [ -n "$SPACK_VERSION" ]; then git clone  https://github.com/key4hep/spack ; cd spack; git checkout $SPACK_VERSION; cd ..; else git clone --depth 1 https://github.com/key4hep/spack; fi 
 source spack/share/spack/setup-env.sh
# get the right config files to the right places
 cp config/packages.yaml spack/etc/spack/
 mkdir spack/var/spack/repos/key4hep-spack
 cp -r * spack/var/spack/repos/key4hep-spack || true
# clean up git directories for zip
 rm -rf spack/.git
# register k4 package recipes with spack
 echo "repos:" > spack/etc/spack/repos.yaml
 echo ' - $SPACK_ROOT/var/spack/repos/key4hep-spack' >> spack/etc/spack/repos.yaml
 tar -czf key4hep-spack.tar.gz spack
 cp ${PWD}/spack/var/spack/repos/key4hep-spack/config/cvmfs_build/upstreams.yaml spack/etc/spack/
# compiler setup 
 spack load gcc
 spack compiler find --scope site
 tar -czf key4hep-spack_centos7-cvmfs.tar.gz spack
