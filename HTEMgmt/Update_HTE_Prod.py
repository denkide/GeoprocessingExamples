# Import system modules
import sys, string, os, arcpy, datetime, time, traceback, win32api


def cleanUp_Log(logText,logFile):
    # write the log and close it
    logFile.write(logText + "")
    logFile.close()
    return   

# Create the Geoprocessor object
#gp = arcgisscripting.create()

# Load required toolboxes...

# LIVE
arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

#TEST
#arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

#--------------------------------------------------------------
#-- Get the starting time
#--------------------------------------------------------------
start = time.clock()

#--------------------------------------------------------------
#this is the logfile location -- the script location and uploadFeature.log
#--------------------------------------------------------------
logFileLocation = sys.path[0] + "\HTE_SDE_1_prod.log"
logText = ""

#--------------------------------------------------------------
# open the log file for writing
#--------------------------------------------------------------

try:
    logFile = open(logFileLocation,"w")
    logText = logText + "****************************************\nBegin HTE Update :: SDE_1_prod\n****************************************\n"

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

    # Script arguments...
    Target_HTE_BuildingPermits = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Building_Permit" # provide a default value if unspecified
    Target_HTE_Code_Enforcement = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Code_Enforcement" # provide a default value if unspecified
    Target_HTE_Occupational_License = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Occupational_License" # provide a default value if unspecifiedxxx
    Target_HTE_Planning_Zoning = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Planning_Zoning" # provide a default value if unspecified
    
    # Local variables...
    Delete_BP_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Building_Permit"
    Append__BP_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Building_Permit"
    Delete_PZ_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Planning_Zoning"
    Append_PZ_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Planning_Zoning"
    Delete_OL_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Occupational_License"
    Append_OL_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Occupational_License"
    Delete_CE_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Code_Enforcement"
    Append_CE_Results = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.ReferenceData_Urban\\SDE.DBO.HTE_Code_Enforcement"
    Source_VHTEBP = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP"
    Source_VHTECE = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE"
    Source_VHTEOL_ = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL"
    Source_VHTEPZ = "Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ"

    # Process: Delete Features BP...
    arcpy.DeleteFeatures_management(Target_HTE_BuildingPermits)
    
    # Process: Append BP...
    arcpy.Append_management("'Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP'", Target_HTE_BuildingPermits, "NO_TEST", "BPPCB BPPCB true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPPCB,-1,-1;BPPYER BPPYER true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPPYER,-1,-1;BPPCNB BPPCNB true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPPCNB,-1,-1;BPLCID BPLCID true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPLCID,-1,-1;BPTNNB BPTNNB true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPTNNB,-1,-1;BPATYP BPATYP true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPATYP,-1,-1;BPASTS BPASTS true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPASTS,-1,-1;BPASDC BPASDC true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPASDC,-1,-1;BPASDT BPASDT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPASDT,-1,-1;BPADAC BPADAC true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPADAC,-1,-1;BPADAT BPADAT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPADAT,-1,-1;BPAMPN BPAMPN true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAMPN,-1,-1;BPAOCA BPAOCA true true false 8 Double 5 16 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAOCA,-1,-1;BPAPRB BPAPRB true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAPRB,-1,-1;BPATNM BPATNM true true false 25 Text 0 0 ,First,#;BPEVAL BPEVAL true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPEVAL,-1,-1;BPPBLD BPPBLD true true false 1 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPPBLD,-1,-1;BPAPGP BPAPGP true true false 6 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAPGP,-1,-1;BPUSTS BPUSTS true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPUSTS,-1,-1;BPRDCD BPRDCD true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPRDCD,-1,-1;BPASQF BPASQF true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPASQF,-1,-1;BPAPPN BPAPPN true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAPPN,-1,-1;BPAPDS BPAPDS true true false 50 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAPDS,-1,-1;BPAEBY BPAEBY true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEBP,BPAEBY,-1,-1;LOCID LOCID true true false 4 Long 0 10 ,First,#")
    
    # Process: Delete Features CE...
    arcpy.DeleteFeatures_management(Target_HTE_Code_Enforcement)
    
    # Process: Append CE...
    arcpy.Append_management("'Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE'", Target_HTE_Code_Enforcement, "NO_TEST", "CASENBR CASENBR true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,CASENBR,-1,-1;CASESTUS CASESTUS true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,CASESTUS,-1,-1;LAND_ID LAND_ID true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,LAND_ID,-1,-1;CASETYPE CASETYPE true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,CASETYPE,-1,-1;INSPECTR INSPECTR true true false 6 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,INSPECTR,-1,-1;TENANT TENANT true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,TENANT,-1,-1;TENT_NBR TENT_NBR true true false 6 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,TENT_NBR,-1,-1;LOCID LOCID true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTECE,LOCID,-1,-1")
    
    # Process: Delete Features OL...
    arcpy.DeleteFeatures_management(Target_HTE_Occupational_License)
    
    # Process: Append OL...
    arcpy.Append_management("'Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL'", Target_HTE_Occupational_License, "NO_TEST", "OLCTLN OLCTLN true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,OLCTLN,-1,-1;BUSNAME BUSNAME true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,BUSNAME,-1,-1;MAILADD1 MAILADD1 true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,MAILADD1,-1,-1;OLYEAR OLYEAR true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,OLYEAR,-1,-1;STATUS STATUS true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,STATUS,-1,-1;ABDJCD ABDJCD true true false 8 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,ABDJCD,-1,-1;LOCID LOCID true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,LOCID,-1,-1;MAILADD2 MAILADD2 true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,MAILADD2,-1,-1;ZIPCODE ZIPCODE true true false 9 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,ZIPCODE,-1,-1;MAILADD3 MAILADD3 true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,MAILADD3,-1,-1;DELIVPT DELIVPT true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,DELIVPT,-1,-1;BUSACODE BUSACODE true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,BUSACODE,-1,-1;BUSPHNUM BUSPHNUM true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,BUSPHNUM,-1,-1;EMERACD EMERACD true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,EMERACD,-1,-1;EMERPNM EMERPNM true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,EMERPNM,-1,-1;BUSSTAT BUSSTAT true true false 1 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,BUSSTAT,-1,-1;STATDT STATDT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,STATDT,-1,-1;BUSOPTDT BUSOPTDT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,BUSOPTDT,-1,-1;CONTFLG CONTFLG true true false 1 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,CONTFLG,-1,-1;TYPTOWN TYPTOWN true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,TYPTOWN,-1,-1;FEDTXID FEDTXID true true false 9 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEOL,FEDTXID,-1,-1")
    
    # Process: Delete Features PZ...
    arcpy.DeleteFeatures_management(Target_HTE_Planning_Zoning)
    
    # Process: Append PZ...
    arcpy.Append_management("'Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ'", Target_HTE_Planning_Zoning, "NO_TEST", "PZCCB PZCCB true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZCCB,-1,-1;PZPYER PZPYER true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPYER,-1,-1;PZPNBR PZPNBR true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPNBR,-1,-1;PZPDES PZPDES true true false 40 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPDES,-1,-1;PZADAC PZADAC true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZADAC,-1,-1;PZADAT PZADAT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZADAT,-1,-1;PZPTYP PZPTYP true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPTYP,-1,-1;PZPSTS PZPSTS true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPSTS,-1,-1;PZPAL1 PZPAL1 true true false 25 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPAL1,-1,-1;PZPAL2 PZPAL2 true true false 25 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPAL2,-1,-1;PZPPLR PZPPLR true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPPLR,-1,-1;PZPGMP PZPGMP true true false 6 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPGMP,-1,-1;PZDUNT PZDUNT true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZDUNT,-1,-1;PZPSQF PZPSQF true true false 8 Double 0 11 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZPSQF,-1,-1;PZCDBL PZCDBL true true false 8 Double 2 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZCDBL,-1,-1;PZBPNF PZBPNF true true false 1 Text 0 0 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZBPNF,-1,-1;PZUNPC PZUNPC true true false 8 Double 2 10 ,First,#,Database Connections\\xxx@xxx_prod.sde\\SDE.DBO.VHTEPZ,PZUNPC,-1,-1;ABAUCD ABAUCD true true false 4 Long 0 10 ,First,#")
except:
    # get the traceback object
    tb = sys.exc_info()[2]
    
    # tbinfo contains the line number that the code failed on and the code from that line
    tbinfo = traceback.format_tb(tb)[0]

    # concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " +             str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"

    # generate a message string for any geoprocessing tool errors
    msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # return gp messages for use with a script tool
    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    # print messages for use in Python/PythonWin
    print msgs
    logText = logText + "\n\nGP Error: " + str(msgs)
        
    print pymsg
    logText = logText + "\nPython Error: " + str(pymsg)


# get the elapsed time
end = time.clock()
elapsed = end - start

logText = logText + "\n\n\n****************************************\nProcess took: " + str(elapsed) + " seconds \nEnd HTE Update :: SDE_1_prod\n****************************************"

cleanUp_Log(logText,logFile)

print "Process ended"
del arcpy      
