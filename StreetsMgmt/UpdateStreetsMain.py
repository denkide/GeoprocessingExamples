import sys, string, os, arcpy, UpdateStreetsProd2_def ,UpdateStreetsPub2_def, UpdateStreetsProd1_def , UpdateStreetsPub1_def, traceback, smtplib, datetime, time

msgs = ""
pymsg = ""
cartegraphUpdate = "Fail"

start = time.clock()

#this is the logfile location -- the script location and uploadFeature.log
logFileLocation = sys.path[0] + "\UpdateAllStreets.log"
logText = ""

# open the log file for writing
try:
    logFile = open(logFileLocation,"w")
except IOError:
    print "there was an error opening the log file"

try:

    arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

    logText = logText + "*************************\nBegin Update\n**************************\n"

    #------------------------
    # Log -------------------
    # get the current date and time
    now = datetime.datetime.now()

    # add the log text for this step
    logText = logText + "\n"
    logText = logText + "Start the process: " + str(now) + "\n"
    #------------------------
    # End Log ---------------

    #------------------------   
    #Update Prod 2 Streets
    #------------------------
    UpdateStreetsProd2_def.UpdateStreets(arcpy)
    msgs = msgs + "xxx\Prod Streets have been updated successfully.\n\n"
        
    #------------------------
    #Update Pub 2 Streets
    #------------------------    
    try:
        UpdateStreetsPub2_def.UpdateStreets(arcpy)
        msgs = msgs + "xxx\Pub Streets have been updated successfully.\n\n"
                
    except:            
        # get the traceback object
        tb = sys.exc_info()[2]
    
        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]
    
        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in Pub 2 Update\n-----------------------------------------\n" + pymsg
    
    pymsg = ""


    #------------------------
    #Update Prod 1 Streets
    #------------------------        
    try:
        UpdateStreetsProd1_def.UpdateStreets(arcpy)
        msgs = msgs + "xxx-1\Prod Streets have been updated successfully.\n\n"
                
    except:
        # get the traceback object
        tb = sys.exc_info()[2]
     
        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]
     
        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in Prod 1 Update\n-----------------------------------------\n" + pymsg


    #------------------------
    #Update Pub 1 Streets
    #------------------------        
    try:
        UpdateStreetsPub1_def.UpdateStreets(arcpy)
        msgs = msgs + "xxx-1\Pub Streets have been updated successfully.\n\n"
        cartegraphUpdate = "Pass"
                
    except:
       # get the traceback object
        tb = sys.exc_info()[2]
     
        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]    
    
        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in Pub 1 Update\n-----------------------------------------\n" + pymsg
     
    pymsg = ""

except:
    # get the traceback object
    tb = sys.exc_info()[2]

    # tbinfo contains the line number that the code failed on and the code from that line
    tbinfo = traceback.format_tb(tb)[0]

    # concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"

    msgs = msgs + "\nErrors occurred in Prod 2 Update\n----------------------------------\n" + pymsg


#------------------------
# Now - figure out if Cartegraph should be updated
#------------------------
if cartegraphUpdate == "Fail":
    msgs = msgs + "\n\nCartegraph Update Status: Please DO NOT update Cartegraph Data. Please contact GIS."
else:
    msgs = msgs + "\n\nCartegraph Update Status: Please update Cartegraph Data at your convenience."
    
    
#------------------------
# Log -------------------
logText = logText + "\n\n*********************Process finished******************\n\r"
logText = logText + msgs + "\n\n"
#------------------------
# End Log ---------------

#------------------------
# now do the email 
#------------------------
Recipients = ['xxx@xxx.org','xxx@xxx.org']
SMTPServer = '172.16.58.103'
AuthRequired = 0
SMTPUser = ''
SMTPPass = ''
Sender = 'xxx@xxx.org'
Subject = 'Streets Update: Automated Email'

EmailText = ''
EmailText = EmailText + 'This is an automated email from the UpdateAllStreets python process.\n\r\n\r'
EmailText = EmailText + 'The streets are copied from the public safety server at \\\\172.16.217.1\\ecsostreets\\shp\\Streets.shp and moved to all SDE instances.\n\r'
EmailText = EmailText + 'The results of each instance update is below.\n\r\n\r'
EmailText = EmailText + msgs

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (Sender, ", ".join(Recipients), Subject, EmailText)  

Session = smtplib.SMTP(SMTPServer)     
if AuthRequired:
    Session.login(SMTPUser, SMTPPass);
SMTPResult = Session.sendmail(Sender, Recipients, message)
#------------------------
# end email 
#------------------------

#------------------------
# Log -------------------
end = time.clock()
elapsed = end - start

logText = logText + "\n\n\n****************************************\n"
logText = logText + "Process took: " + str(elapsed) + " seconds \n"
logText = logText + "End Update\n**********************************"

# write the log and close it
logFile.write(logText + " --- end.")
logFile.close()
#------------------------
# End Log ---------------

