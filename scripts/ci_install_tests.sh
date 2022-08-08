
# DD4hep
geoPluginRun -h
ddsim -h
ddsim --compactFile $LCGEO/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml  -G -N 10 --gun.particle=mu- --gun.distribution uniform --gun.energy "1*GeV" -O muons.slcio 
# K4FWCore
k4run -h
# K4RecCalorimeter
fccrun $K4RECCALORIMETER/RecFCCeeCalorimeter/tests/options/runCaloSim.py

