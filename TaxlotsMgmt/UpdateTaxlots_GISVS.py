# Import system modules
import sys, string, os, arcgisscripting, datetime, time, traceback, win32api


def cleanUp_Log(logText,logFile):
    # write the log and close it
    logFile.write(logText + "")
    logFile.close()
    return   


# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("E:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


#--------------------------------------------------------------
#-- Get the starting time
#--------------------------------------------------------------
start = time.clock()

#--------------------------------------------------------------
#this is the logfile location -- the script location and uploadFeature.log
#--------------------------------------------------------------
logFileLocation = sys.path[0] + "\TaxlotUpdate_MEDGISVS.log"
logText = ""

#--------------------------------------------------------------
# open the log file for writing
#--------------------------------------------------------------

try:
    logFile = open(logFileLocation,"w")
    logText = logText + "****************************************\nBegin Taxlot Update :: MEDGISVS\n****************************************\n"

    #--------------------------------------------------------------
    # get the current date and time
    #--------------------------------------------------------------
    now = datetime.datetime.now()

    #--------------------------------------------------------------    
    # add the log text for this step
    #--------------------------------------------------------------
    logText = logText + "\n"
    logText = logText + "Start the process: " + str(now) + "\n\n\n"
except IOError:
    print "there was an error opening the log file"

try:       

    # Local variables...
    Delete_Results_Pub1 = "Database Connections\\GISxxx@xxxGISVS.sde\\GIS.DBO.TopologicalData\\GIS.DBO.Taxlots"
    Append_Results_Pub1 = "Database Connections\\GISxxx@xxxGISVS.sde\\GIS.DBO.TopologicalData\\GIS.DBO.Taxlots"
    Delete_TL_Pub1 = "Database Connections\\GISxxx@xxxGISVS.sde\\GIS.DBO.TopologicalData\\GIS.DBO.Taxlots"
    JACKSON_taxlots = "C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots"
    Append_Target_Pub1 = "Database Connections\\GISxxx@xxxGISVS.sde\\GIS.DBO.TopologicalData\\GIS.DBO.Taxlots"

    # Process: Delete Features...
    gp.DeleteFeatures_management(Delete_TL_Pub1)

    # Process: Append...
    gp.Append_management("'C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots'", Append_Target_Pub1, "NO_TEST", "MAPNUM MAPNUM true true false 9 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,MAPNUM,-1,-1;TAXLOT TAXLOT true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,TAXLOT,-1,-1;MAPNTAX MAPNTAX true true false 14 Text 0 0 ,First,#;EXTZERO EXTZERO true true false 2 Text 0 0 ,First,#;MPNUM MPNUM true true false 2 Short 0 5 ,First,#;GIS_AREA GIS_AREA true true false 8 Double 8 38 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,GIS_AREA,-1,-1;MAPLOT MAPLOT true true false 16 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,MAPLOT,-1,-1;ACCOUNT ACCOUNT true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ACCOUNT,-1,-1;LOTTYPE LOTTYPE true true false 4 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,LOTTYPE,-1,-1;FEEOWNER FEEOWNER true true false 29 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,FEEOWNER,-1,-1;CONTRACT CONTRACT true true false 29 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,CONTRACT,-1,-1;INCAREOF INCAREOF true true false 29 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,INCAREOF,-1,-1;ADDRESS1 ADDRESS1 true true false 29 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ADDRESS1,-1,-1;ADDRESS2 ADDRESS2 true true false 29 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ADDRESS2,-1,-1;CITY CITY true true false 19 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,CITY,-1,-1;STATE STATE true true false 4 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,STATE,-1,-1;ZIPCODE ZIPCODE true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ZIPCODE,-1,-1;COMMSQFT COMMSQFT true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,COMMSQFT,-1,-1;ACREAGE ACREAGE true true false 8 Double 8 38 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ACREAGE,-1,-1;IMPVALUE IMPVALUE true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,IMPVALUE,-1,-1;LANDVALUE LANDVALUE true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,LANDVALUE,-1,-1;LOTDEPTH LOTDEPTH true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,LOTDEPTH,-1,-1;LOTWIDTH LOTWIDTH true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,LOTWIDTH,-1,-1;PROPCLASS PROPCLASS true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,PROPCLASS,-1,-1;ADDRESSNUM ADDRESSNUM true true false 8 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ADDRESSNUM,-1,-1;STREETNAME STREETNAME true true false 22 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,STREETNAME,-1,-1;BUILDCODE BUILDCODE true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,BUILDCODE,-1,-1;YEARBLT YEARBLT true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,YEARBLT,-1,-1;TAXCODE TAXCODE true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,TAXCODE,-1,-1;ASSESSIMP ASSESSIMP true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ASSESSIMP,-1,-1;ASSESSLAND ASSESSLAND true true false 4 Long 0 10 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ASSESSLAND,-1,-1;MAINTENANC MAINTENANC true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,MAINTENANC,-1,-1;TM_MAPLOT TM_MAPLOT true true false 18 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,TM_MAPLOT,-1,-1;SCHEDULECO SCHEDULECO true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,SCHEDULECO,-1,-1;NEIGHBORHO NEIGHBORHO true true false 2 Short 0 5 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,NEIGHBORHO,-1,-1;OWNERSORT OWNERSORT true true false 5 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,OWNERSORT,-1,-1;ADDSORT ADDSORT true true false 5 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,ADDSORT,-1,-1;TRSSORT TRSSORT true true false 5 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,TRSSORT,-1,-1;SITEADD SITEADD true true false 36 Text 0 0 ,First,#,C:\\Documents and Settings\\All Users\\Application Data\\ESRI\\ArcCatalog\\JacksonCounty_SDE.sde\\JACKSON.taxlots,SITEADD,-1,-1;area area false false true 0 Double 0 0 ,First,#;len len false false true 0 Double 0 0 ,First,#")

    # Process: Analyze...
    gp.Analyze_management(Append_Target_Pub1, "BUSINESS;FEATURE;ADDS;DELETES")
    
except:
    # get the traceback object
    tb = sys.exc_info()[2]
    
    # tbinfo contains the line number that the code failed on and the code from that line
    tbinfo = traceback.format_tb(tb)[0]

    # concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " +             str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"

    # generate a message string for any geoprocessing tool errors
    msgs = "GP ERRORS:\n" + gp.GetMessages(2) + "\n"

    # return gp messages for use with a script tool
    gp.AddError(msgs)
    gp.AddError(pymsg)

    # print messages for use in Python/PythonWin
    print msgs
    logText = logText + "\n\nGP Error: " + str(msgs)
        
    print pymsg
    logText = logText + "\nPython Error: " + str(pymsg)


# get the elapsed time
end = time.clock()
elapsed = end - start

logText = logText + "\n\n\n****************************************\nProcess took: " + str(elapsed) + " seconds \nEnd Taxlot Update :: MEDGISVS\n****************************************"

cleanUp_Log(logText,logFile)

print "Process ended"
del gp      

