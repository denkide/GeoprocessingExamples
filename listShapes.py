import os, fnmatch, arcpy

StartDir = "Z:" # Don't use trailing slashes    
OutputFileName = "LomakatsiShapes.txt"
tempName = os.path.join(StartDir, OutputFileName + ".txt") # os.path.join for creating paths
fc = ""
# use with to ensure closure
with open(tempName, 'w') as outFile:

    for root, dirs, files in arcpy.da.Walk(StartDir, datatype='FeatureClass'):
        # Modify dirs in place to skip file GDBs
        dirs[:] = [d for d in dirs if not d.endswith(".gdb")]
        for f in fnmatch.filter(files, "*.shp"):
            fc = os.path.join(root, f)
            desc = arcpy.Describe(fc)

            try:
                sr = desc.spatialReference
                if sr is None:
                    outFile.write(fc + " is none \n")        
                else:
                    try:
                        outFile.write(fc + "------" + sr.Name + "\n")
                    except:
                        outFile.write(fc + " is an err 1 \n")        
            except:
                outFile.write(fc + " is an err 2 \n")        

