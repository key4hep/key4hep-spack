# Spack repo for HEP software packaging

Initial setup like:

```bash
cd /path/to/big/disk
git clone https://github.com/LLNL/spack.git
git clone https://github.com/HEP-SF/hsf-spack-repo.git
cd spack
./bin/spack compiler add /usr/bin/gcc
./bin/spack repo add /path/to/big/disk/hsf-spack-repo
```

Exercise:

```bash
./bin/spack info root
./bin/spack install root
```

