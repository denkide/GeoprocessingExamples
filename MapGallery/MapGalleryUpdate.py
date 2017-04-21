import sys, string, os, datetime, time, traceback, win32api, shutil

start = time.clock()

copyFrom = 'I:\\Maps\\Map_Gallery\\'
copyTo = 'L:\\'

#this is the logfile location -- the script location and uploadFeature.log
logFileLocation = sys.path[0] + "\MapGalleryUpdate.log"
logText = ""

# open the log file for writing
try:
    logFile = open(logFileLocation,"w")
except IOError:
    print "there was an error opening the log file"

logText = logText + "****************************************\n"
logText = logText + "Begin Map Gallery Update"
logText = logText + "\n****************************************\n\n"

logText = logText + "\nCopyFrom: " + copyFrom
logText = logText + "\nCopyTo: " + copyTo
logText = logText + "\n\n****************************************\n"

# get the current date and time
now = datetime.datetime.now()

# add the log text for this step
logText = logText + "\n"
logText = logText + "Start the process: " + str(now) + "\n\n\n"    

currentDir = ""

for root,dir,files in os.walk(copyFrom):
    #print "%s has subdirectory %s" % (root, dir)
    currentDir = root[(root.rfind("\\") + 1):]

    if not os.path.exists(copyTo + currentDir):
        os.makedirs(copyTo + currentDir)
    
    print "-------" + root[(root.rfind("\\") + 1):]
    for file in files:
        if file.endswith(".pdf"):
            try:
                shutil.copy(copyFrom + currentDir + "\\" + file, copyTo + currentDir + "\\" + file);
                logText += "\n" + copyTo + currentDir + "\\" + file
            except:
                logText += "\n!!!! ERROR !!! :: " + copyTo + currentDir + "\\" + file

# get the elapsed time
end = time.clock()
elapsed = end - start

logText = logText + "\n\n\n****************************************\n"
logText = logText + "Process took: " + str(elapsed) + " seconds \n"
logText = logText + "End Map Gallery Update"
logText = logText + "\n****************************************"

# write the log and close it
logFile.write(logText + "")
logFile.close()        
