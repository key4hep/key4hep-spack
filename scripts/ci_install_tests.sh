geoPluginRun -h
ddsim -h
k4run -h
ddsim --compactFile $LCGEO/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml  -G -N 10 --gun.particle=mu- --gun.distribution uniform --gun.energy "1*GeV" -O muons.slcio 

