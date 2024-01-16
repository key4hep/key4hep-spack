#!/bin/bash

# Initialize counters
success_count=0
failure_count=0

# Function to run a test and update counters
run_test() {
    local test_name=$1
    local command=$2

    echo "Running test: $test_name"
    eval "$command"
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        echo "Test $test_name passed!"
        ((success_count++))
    else
        echo "Test $test_name failed with exit code $exit_code"
        ((failure_count++))
    fi
    echo
}

# Run tests
run_test "git test" "git clone https://github.com/AIDASoft/DD4hep --depth 1"
cat <<EOF > hello.cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
EOF
run_test "c++ test" "g++ -o hello hello.cpp && ./hello"
run_test "c++17 test" "g++ -std=c++17 -o hello hello.cpp && ./hello"
cat <<EOF > hello.f
      program hello
      print *, "Hello, world!"
      end program hello
EOF
run_test "fortran test" "gfortran -o hello hello.f && ./hello"
run_test "Python test" "python -c 'print(\"Hello, world!\")'"
run_test "Python3 test" "python3 -c 'print(\"Hello, world!\")'"
run_test "Numpy test" "python -c 'import numpy as np; np.random.seed(0); print(np.random.rand(3, 3))'"
run_test "Matplotlib test" "python -c 'import matplotlib.pyplot as plt; plt.plot([1, 2, 3], [1, 2, 3]); plt.show()'"
run_test "Pandas test" "python -c 'import pandas as pd; print(pd.DataFrame([[1, 2], [3, 4]]))'"

cat > macro.C <<EOF
{
    int a = 10;
    int b = 5;
    int sum = a + b;
    std::cout << "The sum of " << a << " and " << b << " is " << sum << std::endl;
    return 0;
}
EOF
run_test "ROOT test" "root -b -q -l macro.C"
cat > root_numpy.py <<EOF
import ROOT
df = ROOT.RDataFrame(10) \
         .Define("x", "(int)rdfentry_") \
         .Define("y", "1.f/(1.f+rdfentry_)")
ROOT.gInterpreter.Declare("""
// Inject the C++ class CustomObject in the C++ runtime.
class CustomObject {
public:
    int x = 42;
};
// Create a function that returns such an object. This is called to fill the dataframe.
CustomObject fill_object() { return CustomObject(); }
""")

df3 = df.Define("custom_object", "fill_object()")
npy5 = df3.AsNumpy()
print("Read-out of C++ objects:\n{}\n".format(npy5["custom_object"]))
print("Access to all methods and data members of the C++ object:\nObject: {}\nAccess data member: custom_object.x = {}\n".format(
    repr(npy5["custom_object"][0]), npy5["custom_object"][0].x))
EOF
run_test "ROOT_numpy test" "python root_numpy.py"
run_test "clang-format test" "echo 'int main() { return 0 ; }' | clang-format | diff - <(echo 'int main() { return 0; }')"

run_test "DD4hep test" "ddsim --compactFile DD4hep/DDDetectors/compact/SiD.xml -G -N 1 --gun.particle=mu- --gun.distribution uniform --gun.energy '1*GeV' -O muons.slcio"
# run_test "podio test" "podio-dump muons.slcio"
# run_test "edm4hep test"
# run_test "k4fwcore test" "k4run -n 10 --input muons.slcio --output output.slcio --processors k4FWCoreTestProcessor"

# Produce more than one output to make sure that all of the desired output
# formats are actually available
# see: https://github.com/key4hep/key4hep-spack/issues/533
#      https://github.com/key4hep/key4hep-spack/issues/549
cat > ee.sin <<EOF
    process ee = e1, E1 => e2, E2
    sqrts = 360 GeV
    n_events = 10
    sample_format = lhef, lcio, hepmc
    simulate (ee)
EOF
run_test "whizard test" "whizard -r ee.sin"

cat > fcc.py <<EOF
import ROOT

ROOT.gSystem.Load("libFCCAnalyses")
ROOT.gInterpreter.Declare("using namespace FCCAnalyses;")
_fcc  = ROOT.dummyLoader

ROOT.gInterpreter.Declare('''\
#include "edm4hep/MCParticleData.h"

ROOT::VecOps::RVec<edm4hep::MCParticleData> gen_particles() {
ROOT::VecOps::RVec<edm4hep::MCParticleData> result;
edm4hep::MCParticleData mcPart;
mcPart.momentum.x = 11;
result.push_back(mcPart);

return result;
}
''')

df = ROOT.RDataFrame(10)
df2 = df.Define("particles", "gen_particles()")
df3 = df2.Define("particles_pt", "MCParticle::get_pt(particles)")
hist = df3.Histo1D("particles_pt")
hist.Print()
EOF
run_test "FCCAnalyses test" "python fcc.py"




# Report results
echo "Tests completed:"
echo "Successes: $success_count"
echo "Failures: $failure_count"

# Fail if there were any failures
if [ $failure_count -gt 0 ]; then
    echo "There were test failures!"
    exit 1
else
    echo "All tests passed!"
    exit 0
fi
