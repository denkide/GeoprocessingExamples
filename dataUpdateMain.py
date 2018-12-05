import shutil, os, arcpy,  traceback, smtplib, datetime, time, os.path

# zipfile, urllib.request,


#---------------------------------------------------
# Global Variables
#---------------------------------------------------
defaultSDELocation = "D:\\ArcGIS_Work\\python\\DataUpdates\\SDE@LomaGIS.sde\\"
defaultDownloadLocation = "D:\\ArcGIS_Work\\Downloads\\"




#def fetchZip(url, dest):
#    tempFile = "temp.zip"
#    with urllib.request.urlopen(url) as response, open(tempFile, 'wb') as out_file:
#        shutil.copyfileobj(response, out_file)
#        with zipfile.ZipFile(tempFile) as zf:
#            zf.extractall(dest)
#            zf.close()
#            out_file.close()

def updateFeatures(inputFeatures, existingFeatures):
    try:
        print "Input: " + inputFeatures

        # Process: Delete Features
        arcpy.DeleteFeatures_management(existingFeatures)
        # Process: Append
        arcpy.Append_management(inputFeatures, existingFeatures, "TEST", "", "")

        print "Exit def"
    except:
        print "Errors occurred while updating: " + existingFeatures
        raise

def main():

    #this is the logfile location -- the script location and uploadFeature.log
    logFileLocation = sys.path[0] + "\Lomakatsi_DataUpdate.log"
    logText = "\n"
    msgs = "\n"
    pymsg = "\n"

    print "Main 1"
    start = time.clock()

    #------------------------
    # Log -------------------
    # get the current date and time
    now = datetime.datetime.now()

    

    # ----------------------------------------------
    # DelNorte Parcels
    #-----------------------------------------------
    #msgs = msgs + "\nBegin DelNorte Parcels"
    try:
        delNorteIn = defaultDownloadLocation + "DelNorte\\DN_Parcels.shp"
        delNorteExisting = defaultSDELocation + "LomaGIS.SDE.CA_DelNorteCounty\\LomaGIS.SDE.CA_DelNorte_Parcels"

        if os.path.isfile(delNorteIn): 
            updateFeatures(delNorteIn, delNorteExisting)
        else:
            msgs = msgs + "\nCannot find: " + delNorteIn
            
    except:
        msgs = msgs + "\nErrors while updating DelNorte parcels"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd DelNorte Parcels"

    # ----------------------------------------------
    # Siskiyou Parcels
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Siskiyou Parcels"
    try:
        siskiyouParcelsIn = defaultDownloadLocation + "Siskiyou\\SiskiyouParcelsNov2017.shp"
        siskiyouParcelsExisting = defaultSDELocation + "LomaGIS.SDE.CA_SiskiyouCounty\\LomaGIS.SDE.CA_Siskiyou_Parcels"

        if os.path.isfile(siskiyouParcelsIn): 
            updateFeatures(siskiyouParcelsIn, siskiyouParcelsExisting)
        else:
            msgs = msgs + "\nCannot find: " + siskiyouParcelsIn
    except:
        msgs = msgs + "\nErrors while updating Siskiyou parcels"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd Siskiyou Parcels"

    # ----------------------------------------------
    # Shasta Parcels
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Shasta Parcels"
    try:
        shastaParcelIn = defaultDownloadLocation + "Shasta\\Parcels.shp"
        shastaParcelExisting = defaultSDELocation + "LomaGIS.SDE.CA_ShastaCounty\\LomaGIS.SDE.CA_Shasta_Parcels"

        if os.path.isfile(defaultDownloadLocation + "Shasta\\Parcels.shp"): 
            updateFeatures(shastaParcelIn, shastaParcelExisting)
        else:
            msgs = msgs + "\nCannot find: " + defaultDownloadLocation + "Shasta\\Parcels.shp"
    except:
        msgs = msgs + "\nErrors while updating Shasta parcels"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd Shasta Parcels"

    # ----------------------------------------------
    # Shasta Roads
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Shasta Roads"
    try:
        shastaRoadsIn = defaultDownloadLocation + "Shasta\\co_roads.shp"
        shastaRoadsExisting = defaultSDELocation + "LomaGIS.SDE.CA_ShastaCounty\\LomaGIS.SDE.CA_Shasta_Roads"

        if os.path.isfile(shastaRoadsIn): 
            updateFeatures(shastaRoadsIn, shastaRoadsExisting)
        else:
            msgs = msgs + "\nCannot find: " + shastaRoadsIn
    except:
        msgs = msgs + "\nErrors while updating Shasta roads"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs

    #msgs = msgs + "\nEnd Shasta Roads"

    # ----------------------------------------------
    # Josephine SiteAddress
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Josephine SiteAddress"
    try:
        josephineSiteAddrIn = defaultDownloadLocation + "Josephine\\JoCo_Site_Address.shp"
        josephineSiteAddrExisting = defaultSDELocation + "LomaGIS.SDE.OR_JosephineCounty\\LomaGIS.SDE.OR_Josephine_Site_Address"

        if os.path.isfile(josephineSiteAddrIn): 
            updateFeatures(josephineSiteAddrIn, josephineSiteAddrExisting)
        else:
            msgs = msgs + "\nCannot find: " + josephineSiteAddrIn
    except:
        msgs = msgs + "\nErrors while updating Josephine SiteAddress"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd Josephine SiteAddress"

    # ----------------------------------------------
    # Josephine Streets
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Josephine Streets"
    try:
        josephineStreetsIn = defaultDownloadLocation + "Josephine\\Joco_Streets.shp"
        josephineStreetsExisting = defaultSDELocation + "LomaGIS.SDE.OR_JosephineCounty\\LomaGIS.SDE.OR_Josephine_Streets"

        if os.path.isfile(josephineStreetsIn): 
            updateFeatures(josephineStreetsIn, josephineStreetsExisting)
        else:
            msgs = msgs + "\nCannot find: " + josephineStreetsIn
    except:
        msgs = msgs + "\nErrors while updating Josephine Streets"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd Josephine Streets"

    # ----------------------------------------------
    # Jackson Streets
    #-----------------------------------------------
    #msgs = msgs + "\nBegin Jackson Streets"
    try:
        jacksonStreetsIn = defaultDownloadLocation + "Jackson\\Streets.shp"
        jacksonStreetsExisting = defaultSDELocation + "LomaGIS.SDE.OR_JacksonCounty\\LomaGIS.SDE.OR_Jackson_Streets"

        if os.path.isfile(jacksonStreetsIn): 
            updateFeatures(jacksonStreetsIn, jacksonStreetsExisting)
        else:
            msgs = msgs + "\nCannot find: " + jacksonStreetsIn
    except:
        msgs = msgs + "\nErrors while updating Jackson Streets"

        # get the traceback object
        tb = sys.exc_info()[2]

        # tbinfo contains the line number that the code failed on and the code from that line
        tbinfo = traceback.format_tb(tb)[0]

        # concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        msgs = msgs + "\nErrors occurred in DelNorte updates\n----------------------------------\n" + pymsg

        print msgs
    #msgs = msgs + "\nEnd Jackson Streets"
    
    if len(msgs) > 0:
        msgs = "Process started at: " + str(now) + "\n" + msgs
        #------------------------
        # Log -------------------
        logText = logText + "\n*********************Process finished******************\n\r"
        logText = logText + msgs + "\n"
        #------------------------
        # End Log ---------------

        #------------------------
        # Log -------------------
        end = time.clock()
        elapsed = end - start

        logText = logText + "\n****************************************\n"
        logText = logText + "Process took: " + str(elapsed) + " seconds \n"
        logText = logText + "End Update\n**********************************"

        # open the log file for writing
        try:
            logFile = open(logFileLocation,"w")
            # write the log and close it
            logFile.write(logText)
            logFile.close()
            #------------------------
            # End Log ---------------
        except IOError:
            print "there was an error opening the log file"




    print "End of all processes"    



main()

    
    
