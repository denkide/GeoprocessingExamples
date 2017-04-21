import sys, string, os, arcpy, traceback, time

def UpdateStreets(arcpy):


    try:
        # Create the Geoprocessor object
        #gp = arcgisscripting.create()

        # Load required toolboxes...
        #gp.AddToolbox("E:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
        #gp.AddToolbox("C:/Documents and Settings/djrenz/Application Data/ESRI/ArcToolbox/My Toolboxes/_David_general.tbx")
        arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

        
        # Local variables...
        Streets_Layer = "dispatchstreets_Copy_Layer"
        Input_Streets = "\\\\172.16.217.1\\ecsostreets\\shp\\Streets.shp"
        Workspace = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.DBTools"
        Med_Streets_Unique_Temp = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique_temp"
        xxx_Streets_Unique_Delete_Results = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Append_Results = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Existing_xxx_Streets_Unique_ = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Append_Prod_2_xxx_Streets_Success = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets"
        xxx_Streets_Delete_Results = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets"
        xxx_Streets = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets"
        Medstreets_Layer = "dispatchstreets_Copy_Layer"
        Delete_Streets_Result_ = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Streets_Append_Success = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Delete_xxx_streets_unique_temp = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique_temp"
        Prod_1_xxx_Streets_Unique_temp = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique_temp"
        Copied_Input_Streets = "F:\\Processes\\UpdateStreets\\Temp\\dispatchstreets_Copy.shp"
        Prod_1_Streets = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Delete_Success = "F:\\Processes\\UpdateStreets\\Temp\\dispatchstreets_Copy.shp"

        #try:
        #    gp.Delete_management(Copied_Input_Streets, "ShapeFile")
        #except:
        #    print "Nothing to delete here : " + Copied_Input_Streets

        time.sleep(10)

        print "Beginning"
        
        try:
            arcpy.Delete_management(Copied_Input_Streets, "")
        except:
            print "Nothing to delete here 2"

        # Process: Copy...
        try:
            arcpy.Copy_management(Input_Streets, Copied_Input_Streets, "ShapeFile")
        except:
            arcpy.Delete_management(Copied_Input_Streets, "")
            arcpy.Copy_management(Input_Streets, Copied_Input_Streets, "ShapeFile")
            
        time.sleep(5)

        # Process: Make Feature Layer...
        arcpy.MakeFeatureLayer_management(Copied_Input_Streets, Streets_Layer, "", Workspace, "IDNUM IDNUM VISIBLE NONE;PREFIX PREFIX VISIBLE NONE;STREETNAME STREETNAME VISIBLE NONE;STREETTYPE STREETTYPE VISIBLE NONE;SUFFIX SUFFIX VISIBLE NONE;CFCC CFCC VISIBLE NONE;CITY_L CITY_L VISIBLE NONE;CITY_R CITY_R VISIBLE NONE;FROMLEFT FROMLEFT VISIBLE NONE;TOLEFT TOLEFT VISIBLE NONE;FROMRIGHT FROMRIGHT VISIBLE NONE;TORIGHT TORIGHT VISIBLE NONE;ZIP_L ZIP_L VISIBLE NONE;ZIP_R ZIP_R VISIBLE NONE;POLICE_L POLICE_L VISIBLE NONE;POLICE_R POLICE_R VISIBLE NONE;FIRE_L FIRE_L VISIBLE NONE;FIRE_R FIRE_R VISIBLE NONE;EMS_L EMS_L VISIBLE NONE;EMS_R EMS_R VISIBLE NONE;P_BEAT_L P_BEAT_L VISIBLE NONE;P_BEAT_R P_BEAT_R VISIBLE NONE;MAP_PAGE1 MAP_PAGE1 VISIBLE NONE;MAP_PAGE2 MAP_PAGE2 VISIBLE NONE;MAP_PAGE3 MAP_PAGE3 VISIBLE NONE;X1 X1 VISIBLE NONE;Y1 Y1 VISIBLE NONE;X2 X2 VISIBLE NONE;Y2 Y2 VISIBLE NONE;TYPE TYPE VISIBLE NONE;LABELTYPE LABELTYPE VISIBLE NONE;LESN LESN VISIBLE NONE;RESN RESN VISIBLE NONE;NAME NAME VISIBLE NONE;STREET STREET VISIBLE NONE;LEGALNAME LEGALNAME VISIBLE NONE;SURF_TYPE SURF_TYPE VISIBLE NONE;SPEED SPEED VISIBLE NONE;LCITY LCITY VISIBLE NONE;RCITY RCITY VISIBLE NONE;ONEWAY ONEWAY VISIBLE NONE;NAMED NAMED VISIBLE NONE;ADDRESSED ADDRESSED VISIBLE NONE;NAMELOW NAMELOW VISIBLE NONE;LENGTH LENGTH VISIBLE NONE;COUNTY COUNTY VISIBLE NONE;REVERSED REVERSED VISIBLE NONE;BLM BLM VISIBLE NONE;USFS USFS VISIBLE NONE;MP_DIST MP_DIST VISIBLE NONE;MP_BEG MP_BEG VISIBLE NONE;MP_END MP_END VISIBLE NONE;ROADNUMB ROADNUMB VISIBLE NONE;FLIPME FLIPME VISIBLE NONE;SHAPE_LENG SHAPE_LENG VISIBLE NONE;TCFCC TCFCC VISIBLE NONE;NEW_TYPE NEW_TYPE VISIBLE NONE")

        print "Make feature layer :: " + Copied_Input_Streets
        
        time.sleep(5)

        # Process: Select Layer By Attribute...
        #gp.SelectLayerByAttribute_management(Streets_Layer, "NEW_SELECTION", "\"POLICE_L\" LIKE 'M%' OR \"POLICE_R\" LIKE 'M%'")
        arcpy.SelectLayerByAttribute_management(Streets_Layer, "NEW_SELECTION", "\"P_L\" LIKE 'M%' OR \"P_R\" LIKE 'M%'")

        print "Select layer by attribute : " + Streets_Layer

        time.sleep(5)

        # Process: Delete...
        arcpy.Delete_management(Prod_1_xxx_Streets_Unique_temp, "FeatureClass")

        time.sleep(5)

        # Process: Dissolve...
        arcpy.Dissolve_management(Medstreets_Layer, Med_Streets_Unique_Temp, "NAME", "", "MULTI_PART", "DISSOLVE_LINES")

        time.sleep(5)

        # Process: Delete Features...
        try:
            arcpy.DeleteFeatures_management(Existing_xxx_Streets_Unique_)
        except:
            print "Delete Existing xxx Streets Unique is a no go."

        time.sleep(5)

        # Process: Append...
        arcpy.Append_management("'Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique_temp'", Existing_xxx_Streets_Unique_, "NO_TEST", "NAME 'NAME' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique_temp,NAME,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#", "")

        time.sleep(5)

        # Process: Delete Features (2)...
        arcpy.DeleteFeatures_management(xxx_Streets)

        time.sleep(5)

    
        arcpy.Append_management("dispatchstreets_Copy_Layer", xxx_Streets, "NO_TEST", "OBJECTID 'OBJECTID' true true false 8 Double 0 10 ,First,#;IDNUM 'IDNUM' true true false 8 Double 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,IDNUM,-1,-1;PREFIX 'PREFIX' true true false 2 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,PREFIX,-1,-1;STREETNAME 'STREETNAME' true true false 30 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREETNAME,-1,-1;STREETTYPE 'STREETTYPE' true true false 4 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREETTYPE,-1,-1;SUFFIX 'SUFFIX' true true false 2 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SUFFIX,-1,-1;CFCC 'CFCC' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CFCC,-1,-1;CITY_L 'CITY_L' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CITY_L,-1,-1;CITY_R 'CITY_R' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CITY_R,-1,-1;FROMLEFT 'FROMLEFT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FROMLEFT,-1,-1;TOLEFT 'TOLEFT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TOLEFT,-1,-1;FROMRIGHT 'FROMRIGHT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FROMRIGHT,-1,-1;TORIGHT 'TORIGHT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TORIGHT,-1,-1;ZIP_L 'ZIP_L' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ZIP_L,-1,-1;ZIP_R 'ZIP_R' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ZIP_R,-1,-1;POLICE_L 'POLICE_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,POLICE_L,-1,-1;POLICE_R 'POLICE_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,POLICE_R,-1,-1;FIRE_L 'FIRE_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FIRE_L,-1,-1;FIRE_R 'FIRE_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FIRE_R,-1,-1;EMS_L 'EMS_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,EMS_L,-1,-1;EMS_R 'EMS_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,EMS_R,-1,-1;P_BEAT_L 'P_BEAT_L' true true false 16 Text 0 0 ,First,#;P_BEAT_R 'P_BEAT_R' true true false 16 Text 0 0 ,First,#;MAP_PAGE1 'MAP_PAGE1' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE1,-1,-1;MAP_PAGE2 'MAP_PAGE2' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE2,-1,-1;MAP_PAGE3 'MAP_PAGE3' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE3,-1,-1;X1 'X1' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,X1,-1,-1;Y1 'Y1' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,Y1,-1,-1;X2 'X2' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,X2,-1,-1;Y2 'Y2' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,Y2,-1,-1;TYPE 'TYPE' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TYPE,-1,-1;LABELTYPE 'LABELTYPE' true true false 8 Double 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LABELTYPE,-1,-1;LESN 'LESN' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LESN,-1,-1;RESN 'RESN' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,RESN,-1,-1;NAME 'NAME' true true false 30 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAME,-1,-1;STREET 'STREET' true true false 72 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREET,-1,-1;LEGALNAME 'LEGALNAME' true true false 36 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LEGALNAME,-1,-1;SURF_TYPE 'SURF_TYPE' true true false 20 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SURF_TYPE,-1,-1;SPEED 'SPEED' true true false 8 Double 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SPEED,-1,-1;LCITY 'LCITY' true true false 32 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LCITY,-1,-1;RCITY 'RCITY' true true false 32 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,RCITY,-1,-1;ONEWAY 'ONEWAY' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ONEWAY,-1,-1;NAMED 'NAMED' true true false 36 Date 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAMED,-1,-1;ADDRESSED 'ADDRESSED' true true false 36 Date 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ADDRESSED,-1,-1;NAMELOW 'NAMELOW' true true false 36 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAMELOW,-1,-1;SOURCETHM 'SOURCETHM' true true false 16 Text 0 0 ,First,#;LENGTH 'LENGTH' true true false 8 Double 0 19 ,First,#;COUNTY 'COUNTY' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,COUNTY,-1,-1;REVERSED 'REVERSED' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,REVERSED,-1,-1;BLM 'BLM' true true false 12 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,BLM,-1,-1;USFS 'USFS' true true false 12 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,USFS,-1,-1;MP_DIST 'MP_DIST' true true false 8 Double 4 14 ,First,#;MP_BEG 'MP_BEG' true true false 8 Double 4 14 ,First,#;MP_END 'MP_END' true true false 8 Double 4 14 ,First,#;ROADNUMB 'ROADNUMB' true true false 4 Long 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ROADNUMB,-1,-1;FLIPME 'FLIPME' true true false 4 Long 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FLIPME,-1,-1;SHAPE_LENG 'SHAPE_LENG' true true false 8 Double 11 19 ,First,#;CROSS1 'CROSS1' true true false 254 Text 0 0 ,First,#;CROSS2 'CROSS2' true true false 254 Text 0 0 ,First,#;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#", "")

        print "Append : " + xxx_Streets
        
        time.sleep(5)

        # Process: Delete Features (4)...
        arcpy.DeleteFeatures_management(Prod_1_Streets)

        time.sleep(5)

        # Process: Append (4)...
        arcpy.Append_management("F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp", Prod_1_Streets, "NO_TEST", "IDNUM 'IDNUM' true true false 4 Long 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,IDNUM,-1,-1;PREFIX 'PREFIX' true true false 2 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,PREFIX,-1,-1;STREETNAME 'STREETNAME' true true false 30 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREETNAME,-1,-1;STREETTYPE 'STREETTYPE' true true false 4 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREETTYPE,-1,-1;SUFFIX 'SUFFIX' true true false 2 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SUFFIX,-1,-1;CFCC 'CFCC' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CFCC,-1,-1;CITY_L 'CITY_L' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CITY_L,-1,-1;CITY_R 'CITY_R' true true false 3 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,CITY_R,-1,-1;FROMLEFT 'FROMLEFT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FROMLEFT,-1,-1;TOLEFT 'TOLEFT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TOLEFT,-1,-1;FROMRIGHT 'FROMRIGHT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FROMRIGHT,-1,-1;TORIGHT 'TORIGHT' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TORIGHT,-1,-1;ZIP_L 'ZIP_L' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ZIP_L,-1,-1;ZIP_R 'ZIP_R' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ZIP_R,-1,-1;POLICE_L 'POLICE_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,POLICE_L,-1,-1;POLICE_R 'POLICE_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,POLICE_R,-1,-1;FIRE_L 'FIRE_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FIRE_L,-1,-1;FIRE_R 'FIRE_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FIRE_R,-1,-1;EMS_L 'EMS_L' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,EMS_L,-1,-1;EMS_R 'EMS_R' true true false 15 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,EMS_R,-1,-1;P_BEAT_L 'P_BEAT_L' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,P_BEAT_L,-1,-1;P_BEAT_R 'P_BEAT_R' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,P_BEAT_R,-1,-1;MAP_PAGE1 'MAP_PAGE1' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE1,-1,-1;MAP_PAGE2 'MAP_PAGE2' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE2,-1,-1;MAP_PAGE3 'MAP_PAGE3' true true false 10 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MAP_PAGE3,-1,-1;X1 'X1' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,X1,-1,-1;Y1 'Y1' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,Y1,-1,-1;X2 'X2' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,X2,-1,-1;Y2 'Y2' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,Y2,-1,-1;TYPE 'TYPE' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,TYPE,-1,-1;LABELTYPE 'LABELTYPE' true true false 4 Long 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LABELTYPE,-1,-1;LESN 'LESN' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LESN,-1,-1;RESN 'RESN' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,RESN,-1,-1;NAME 'NAME' true true false 30 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAME,-1,-1;STREET 'STREET' true true false 72 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,STREET,-1,-1;LEGALNAME 'LEGALNAME' true true false 36 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LEGALNAME,-1,-1;SURF_TYPE 'SURF_TYPE' true true false 20 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SURF_TYPE,-1,-1;SPEED 'SPEED' true true false 4 Long 0 10 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SPEED,-1,-1;LCITY 'LCITY' true true false 32 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LCITY,-1,-1;RCITY 'RCITY' true true false 32 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,RCITY,-1,-1;ONEWAY 'ONEWAY' true true false 5 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ONEWAY,-1,-1;NAMED 'NAMED' true true false 36 Date 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAMED,-1,-1;ADDRESSED 'ADDRESSED' true true false 36 Date 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ADDRESSED,-1,-1;NAMELOW 'NAMELOW' true true false 36 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NAMELOW,-1,-1;SOURCETHM 'SOURCETHM' true true false 16 Text 0 0 ,First,#;LENGTH 'LENGTH' true true false 8 Double 0 19 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,LENGTH,-1,-1;COUNTY 'COUNTY' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,COUNTY,-1,-1;REVERSED 'REVERSED' true true false 16 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,REVERSED,-1,-1;BLM 'BLM' true true false 12 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,BLM,-1,-1;USFS 'USFS' true true false 12 Text 0 0 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,USFS,-1,-1;MP_DIST 'MP_DIST' true true false 8 Double 4 12 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MP_DIST,-1,-1;MP_BEG 'MP_BEG' true true false 8 Double 4 12 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MP_BEG,-1,-1;MP_END 'MP_END' true true false 8 Double 4 12 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,MP_END,-1,-1;ROADNUMB 'ROADNUMB' true true false 2 Short 0 5 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,ROADNUMB,-1,-1;FLIPME 'FLIPME' true true false 2 Short 0 5 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,FLIPME,-1,-1;SHAPE_LENG 'SHAPE_LENG' true true false 8 Double 11 18 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,SHAPE_LENG,-1,-1;CROSS2 'CROSS2' true true false 254 Text 0 0 ,First,#;CROSS1 'CROSS1' true true false 254 Text 0 0 ,First,#;New_Type 'New_Type' true true false 8 Double 8 38 ,First,#,F:\\Processes\\UpdateStreets\Temp\\dispatchstreets_Copy.shp,NEW_TYPE,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#", "")

        time.sleep(5)

        # Process: Delete (2)...
        arcpy.Delete_management(Copied_Input_Streets, "ShapeFile")

        del arcpy

    except:
        print 'Errors occurred in UpdateStreetsProd2_def'
        raise


def Test():
    try:
        raise RuntimeError("raising the error in Prod2")
    except RuntimeError:
        raise




    
