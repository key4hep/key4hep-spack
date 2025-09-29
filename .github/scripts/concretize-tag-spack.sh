cd /
if [ -z "$1" ]; then
  tag=$(curl -s https://api.github.com/repos/spack/spack/releases/latest | grep '"tag_name":' | cut -d'"' -f4)
else
  tag="$1"
fi
echo "Checking out the spack tag: $tag"
git clone https://github.com/spack/spack -q -b $tag
source spack/share/spack/setup-env.sh

cd /spack
# git checkout $(cat /key4hep-spack/.latest-commit)
# source /key4hep-spack/.cherry-pick

spack repo set --destination /spack-packages builtin
spack repo add key4hep-spack
git clone https://github.com/spack/spack-packages
cd /key4hep-spack/environments/key4hep-base

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
