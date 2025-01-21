cd /
latest=$(curl -s https://api.github.com/repos/spack/spack/releases/latest | jq -r .tag_name)
echo "Latest spack release: $latest"
git clone https://github.com/spack/spack -q -b $latest
source spack/share/spack/setup-env.sh

cd /spack
# git checkout $(cat /key4hep-spack/.latest-commit)
# source /key4hep-spack/.cherry-pick

if [ "${{ matrix.build_type }}" = "release" ]; then
    env=key4hep-release-opt
elif [ "${{ matrix.build_type }}" = "nightly" ]; then
    env=key4hep-nightly-opt
else
    echo "Unknown build type"
    exit 1
fi
cd /key4hep-spack/environments/${env}

echo "========="
echo "spack.yaml"
cat spack.yaml
echo "========="
echo "packages.yaml"
cat packages.yaml
echo "========="
echo "key4hep-common/packages.yaml"
cat /key4hep-spack/environments/key4hep-common/packages.yaml
echo "========="

spack env activate .
spack concretize
