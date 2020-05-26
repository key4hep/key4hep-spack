# Install the key4hep software stack on the cvmfs publisher


# path to k4-spack repo
export K4SPACK=$HOME/k4-spack
export K4CONFIG=$K4SPACK/config/latest/x86_64-centos7-gcc8-opt

export SPACKCMD="python $HOME/spack/bin/spack -C $K4CONFIG"

echo "install from pre-built binaries ..."
$SPACKCMD mirror add eos_buildcache http://key4hep.web.cern.ch/key4hep/spack_build/mirror/${DATE}/
$SPACKCMD buildcache install -o -u key4hep-stack 

echo " create view in directory named after date..."
echo " remove existing view in case there is one"
rm -r /cvmfs/sw-nightlies.hsf.org/key4hep/views/`date -I`/x86_64-centos7-gcc8-opt/ || true
$SPACKCMD  view  symlink -i /cvmfs/sw-nightlies.hsf.org/key4hep/views/`date -I`/x86_64-centos7-gcc8-opt/ key4hep-stack
cp $K4SPACK/scripts/setup_view/setup.sh /cvmfs/sw-nightlies.hsf.org/key4hep/views/`date -I`/x86_64-centos7-gcc8-opt/

echo "create view in directory 'latest'..."
echo "remove existing view in case there is one"
rm -r /cvmfs/sw-nightlies.hsf.org/key4hep/views/latest/x86_64-centos7-gcc8-opt/ || true
$SPACKCMD view  symlink -i /cvmfs/sw-nightlies.hsf.org/key4hep/views/latest/x86_64-centos7-gcc8-opt/ key4hep-stack
cp $K4SPACK/scripts/setup_view/setup.sh /cvmfs/sw-nightlies.hsf.org/key4hep/views/latest/x86_64-centos7-gcc8-opt/
