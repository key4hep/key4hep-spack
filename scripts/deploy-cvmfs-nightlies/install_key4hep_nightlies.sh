#rsync -axv --inplace --delete --copy-links  -e "ssh -T  -o Compression=no -o StrictHostKeyChecking=no -o GSSAPIAuthentication=yes -o GSSAPITrustDNS=yes" gitlab-runner@k4-centos7-03:/cvmfs/sw-nightlies.hsf.org/spackages2/ /cvmfs/sw-nightlies.hsf.org/spackages2/

rsync -axv --inplace --delete  -e "ssh -T  -o Compression=no -o StrictHostKeyChecking=no -o GSSAPIAuthentication=yes -o GSSAPITrustDNS=yes" gitlab-runner@k4-centos7-03:/cvmfs/sw-nightlies.hsf.org/spackages6/ /cvmfs/sw-nightlies.hsf.org/spackages6/

# create symlink
latest_version=$(ls -r1  --ignore='*latest*' /cvmfs/sw-nightlies.hsf.org/spackages6/key4hep-stack/ | head -n 1)
rm /cvmfs/sw-nightlies.hsf.org/spackages6/key4hep-stack/master-latest || true
ln -s -T /cvmfs/sw-nightlies.hsf.org/spackages6/key4hep-stack/${latest_version}/ /cvmfs/sw-nightlies.hsf.org/spackages6/key4hep-stack/master-latest

