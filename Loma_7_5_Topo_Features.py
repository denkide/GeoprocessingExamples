import os, fnmatch, arcpy

StartDir = "Z:/7.5_topo/" # Don't use trailing slashes    
OutputFileName = "Loma_7_5_topo.txt"
tempName = os.path.join("Z:/", OutputFileName + ".txt") # os.path.join for creating paths
fc = ""
# use with to ensure closure
with open(tempName, 'w') as outFile:

    r = []
    subdirs = [x[0] for x in os.walk(StartDir)]

    for subdir in subdirs:
        if str(subdir).endswith('gdb'):
            #print "--------- " + str(subdir) + " -------------"
            arcpy.env.workspace = subdir

            #print "processing: " + arcpy.env.workspace
            outFile.write(arcpy.env.workspace + " \n")
            
            fcs = []
            for fds in arcpy.ListDatasets('','feature') + ['']:
                for fc in arcpy.ListFeatureClasses('','',fds):
                    desc = arcpy.Describe(fc)
                    sr = desc.spatialReference
                    if sr is None:
                        outFile.write(fc + " is none \n")        
                    else:
                        try:
                            outFile.write(arcpy.env.workspace + ' ---- ' + fds + '/' + fc + " --- " + sr.Name + "\n")
                        except:
                            outFile.write(fc + " is an err 1 \n")               
                                
        else:
            x = [ f for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir,f)) ]

            for file in x:
                #print(file)
                if file != None:
                    if file.endswith("shp"):
                        try:
                            shpFC = os.path.join(subdir + "/",file)
                            desc = arcpy.Describe(shpFC)
                            sr = desc.spatialReference
                            if sr is None:
                                outFile.write(shpFC + " is none \n")        
                            else:
                                outFile.write(subdir + "/" + file + " --- " + sr.Name + "\n")                         
                        except:
                                outFile.write(subdir + "/" + file + " --- failed")

                    if file.endswith("sid"):
                        outFile.write(subdir + "/" + file + " \n")        

                    
