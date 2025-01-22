cd /
if [ -z "$2" ]; then
  tag=$(curl -s https://api.github.com/repos/spack/spack/releases/latest | grep '"tag_name":' | cut -d'"' -f4)
else
  tag="$2"
fi
echo "Checking out the spack tag: $tag"
git clone https://github.com/spack/spack -q -b $tag
source spack/share/spack/setup-env.sh

cd /spack
# git checkout $(cat /key4hep-spack/.latest-commit)
# source /key4hep-spack/.cherry-pick

if [ "$1" = "release" ]; then
    env=key4hep-release-opt
elif [ "$1" = "nightly" ]; then
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
