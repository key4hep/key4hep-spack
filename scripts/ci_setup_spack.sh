# set up spack inside the k4-spack repo
 if [ -n "$SPACK_VERSION" ]; then git clone  https://github.com/key4hep/spack ; cd spack; git checkout $SPACK_VERSION; cd ..; else git clone --depth 1 https://github.com/key4hep/spack; fi 
 source spack/share/spack/setup-env.sh
