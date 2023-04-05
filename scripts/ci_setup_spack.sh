if [ -n "$SPACK_VERSION" ]; then
    git clone https://github.com/key4hep/spack -b $SPACK_VERSION --depth 1
else
    git clone --depth 1 https://github.com/key4hep/spack
fi
 source spack/share/spack/setup-env.sh
