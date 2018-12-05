import os, fnmatch, arcpy

StartDir = "Z:/" # Don't use trailing slashes    
OutputFileName = "Loma_All.txt"
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
                    try:
                        desc = arcpy.Describe(fc)
                        sr = desc.spatialReference
                        if sr is None:
                            outFile.write(fc + " is none \t\t\n")        
                        else:
                            outFile.write(arcpy.env.workspace + '\t' + fds + '/' + fc + "\t" + sr.Name + "\n")
                    except:
                        outFile.write(fc + " is an err 1 \t\t\n")               
                                
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
                                outFile.write(shpFC + " is none \t\t\n")        
                            else:
                                outFile.write(subdir + "/\t" + file + "\t" + sr.Name + "\n")                         
                        except:
                                outFile.write(subdir + "/\t" + file + "\tfailed\n")
                    if file.endswith("sid"):
                        outFile.write(subdir + "/\t" + file + " \t\n")
