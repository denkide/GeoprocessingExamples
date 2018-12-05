import os, fnmatch, arcpy

StartDir = "Z:/" # Don't use trailing slashes    
OutputFileName = "LomakatsiGDBFeatures.txt"
tempName = os.path.join(StartDir, OutputFileName + ".txt") # os.path.join for creating paths
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
                    outFile.write(arcpy.env.workspace + ' ---- ' + fds + '/' + fc + " \n")


    
