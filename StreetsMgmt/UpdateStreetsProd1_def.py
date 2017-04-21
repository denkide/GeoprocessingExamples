import sys, string, os, arcpy, traceback

def UpdateStreets(arcpy):
    try:
        # Create the Geoprocessor object
        #gp = arcgisscripting.create()

        # Load required toolboxes...
        #gp.AddToolbox("E:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
        arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

        # Local variables...
        Prod_1_Streets_Append_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Prod_1_xxxStreets_Append_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets"
        Prod_1_xxx_Pavement_Streets_Append_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Pavement_Streets"
        Prod_1_xxx_Streets_Unique_Append_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Prod_1_Streets_Delete_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Prod_1_xxxStreets_Delete_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets"
        Prod_1_xxx_Streets_Unique_Delete_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Prod_1_xxx_Pavement_Streets_Delete_Success = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Pavement_Streets"
        Prod_1_Streets = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Prod_2_Streets = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets"
        Prod_1_xxxStreets = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets"
        Prod_2_xxxStreets = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets"
        Prod_1_xxx_Streets_Unique = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Prod_2_xxx_Streets_Unique = "Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique"
        Prod_1_xxx_Pavement_Streets = "Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Pavement_Streets"

        # Process: Delete Features...
        arcpy.DeleteFeatures_management(Prod_1_Streets)

        # Process: Append...
        arcpy.Append_management("'Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets'", Prod_1_Streets, "NO_TEST", "IDNUM 'IDNUM' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,IDNUM,-1,-1;PREFIX 'PREFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,PREFIX,-1,-1;STREETNAME 'STREETNAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,STREETNAME,-1,-1;STREETTYPE 'STREETTYPE' true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,STREETTYPE,-1,-1;SUFFIX 'SUFFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,SUFFIX,-1,-1;CFCC 'CFCC' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,CFCC,-1,-1;CITY_L 'CITY_L' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,CITY_L,-1,-1;CITY_R 'CITY_R' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,CITY_R,-1,-1;FROMLEFT 'FROMLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,FROMLEFT,-1,-1;TOLEFT 'TOLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,TOLEFT,-1,-1;FROMRIGHT 'FROMRIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,FROMRIGHT,-1,-1;TORIGHT 'TORIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,TORIGHT,-1,-1;ZIP_L 'ZIP_L' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,ZIP_L,-1,-1;ZIP_R 'ZIP_R' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,ZIP_R,-1,-1;POLICE_L 'POLICE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,POLICE_L,-1,-1;POLICE_R 'POLICE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,POLICE_R,-1,-1;FIRE_L 'FIRE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,FIRE_L,-1,-1;FIRE_R 'FIRE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,FIRE_R,-1,-1;EMS_L 'EMS_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,EMS_L,-1,-1;EMS_R 'EMS_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,EMS_R,-1,-1;P_BEAT_L 'P_BEAT_L' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,P_BEAT_L,-1,-1;P_BEAT_R 'P_BEAT_R' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,P_BEAT_R,-1,-1;MAP_PAGE1 'MAP_PAGE1' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MAP_PAGE1,-1,-1;MAP_PAGE2 'MAP_PAGE2' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MAP_PAGE2,-1,-1;MAP_PAGE3 'MAP_PAGE3' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MAP_PAGE3,-1,-1;X1 'X1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,X1,-1,-1;Y1 'Y1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,Y1,-1,-1;X2 'X2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,X2,-1,-1;Y2 'Y2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,Y2,-1,-1;TYPE 'TYPE' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,TYPE,-1,-1;LABELTYPE 'LABELTYPE' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,LABELTYPE,-1,-1;LESN 'LESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,LESN,-1,-1;RESN 'RESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,RESN,-1,-1;NAME 'NAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,NAME,-1,-1;STREET 'STREET' true true false 72 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,STREET,-1,-1;LEGALNAME 'LEGALNAME' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,LEGALNAME,-1,-1;SURF_TYPE 'SURF_TYPE' true true false 20 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,SURF_TYPE,-1,-1;SPEED 'SPEED' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,SPEED,-1,-1;LCITY 'LCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,LCITY,-1,-1;RCITY 'RCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,RCITY,-1,-1;ONEWAY 'ONEWAY' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,ONEWAY,-1,-1;NAMED 'NAMED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,NAMED,-1,-1;ADDRESSED 'ADDRESSED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,ADDRESSED,-1,-1;NAMELOW 'NAMELOW' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,NAMELOW,-1,-1;SOURCETHM 'SOURCETHM' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,SOURCETHM,-1,-1;LENGTH 'LENGTH' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,LENGTH,-1,-1;COUNTY 'COUNTY' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,COUNTY,-1,-1;REVERSED 'REVERSED' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,REVERSED,-1,-1;BLM 'BLM' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,BLM,-1,-1;USFS 'USFS' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,USFS,-1,-1;MP_DIST 'MP_DIST' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MP_DIST,-1,-1;MP_BEG 'MP_BEG' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MP_BEG,-1,-1;MP_END 'MP_END' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,MP_END,-1,-1;ROADNUMB 'ROADNUMB' true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,ROADNUMB,-1,-1;FLIPME 'FLIPME' true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,FLIPME,-1,-1;SHAPE_LENG 'SHAPE_LENG' true true false 8 Double 11 18 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,SHAPE_LENG,-1,-1;CROSS2 'CROSS2' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,CROSS2,-1,-1;CROSS1 'CROSS1' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,CROSS1,-1,-1;New_type 'New_type' true true false 8 Double 8 38 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,New_Type,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.ReferenceData_County\\SDE.DBO.Streets,Shape.len,-1,-1", "")

        # Process: Delete Features (2)...
        arcpy.DeleteFeatures_management(Prod_1_xxxStreets)

        # Process: Append (2)...
        arcpy.Append_management("'Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets'", Prod_1_xxxStreets, "NO_TEST", "OBJECTID 'OBJECTID' true true false 8 Double 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,OBJECTID,-1,-1;IDNUM 'IDNUM' true true false 8 Double 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,IDNUM,-1,-1;PREFIX 'PREFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,PREFIX,-1,-1;STREETNAME 'STREETNAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,STREETNAME,-1,-1;STREETTYPE 'STREETTYPE' true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,STREETTYPE,-1,-1;SUFFIX 'SUFFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,SUFFIX,-1,-1;CFCC 'CFCC' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,CFCC,-1,-1;CITY_L 'CITY_L' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,CITY_L,-1,-1;CITY_R 'CITY_R' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,CITY_R,-1,-1;FROMLEFT 'FROMLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,FROMLEFT,-1,-1;TOLEFT 'TOLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,TOLEFT,-1,-1;FROMRIGHT 'FROMRIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,FROMRIGHT,-1,-1;TORIGHT 'TORIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,TORIGHT,-1,-1;ZIP_L 'ZIP_L' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,ZIP_L,-1,-1;ZIP_R 'ZIP_R' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,ZIP_R,-1,-1;POLICE_L 'POLICE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,POLICE_L,-1,-1;POLICE_R 'POLICE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,POLICE_R,-1,-1;FIRE_L 'FIRE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,FIRE_L,-1,-1;FIRE_R 'FIRE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,FIRE_R,-1,-1;EMS_L 'EMS_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,EMS_L,-1,-1;EMS_R 'EMS_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,EMS_R,-1,-1;P_BEAT_L 'P_BEAT_L' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,P_BEAT_L,-1,-1;P_BEAT_R 'P_BEAT_R' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,P_BEAT_R,-1,-1;MAP_PAGE1 'MAP_PAGE1' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE1,-1,-1;MAP_PAGE2 'MAP_PAGE2' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE2,-1,-1;MAP_PAGE3 'MAP_PAGE3' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE3,-1,-1;X1 'X1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,X1,-1,-1;Y1 'Y1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,Y1,-1,-1;X2 'X2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,X2,-1,-1;Y2 'Y2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,Y2,-1,-1;TYPE 'TYPE' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,TYPE,-1,-1;LABELTYPE 'LABELTYPE' true true false 8 Double 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,LABELTYPE,-1,-1;LESN 'LESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,LESN,-1,-1;RESN 'RESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,RESN,-1,-1;NAME 'NAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,NAME,-1,-1;STREET 'STREET' true true false 72 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,STREET,-1,-1;LEGALNAME 'LEGALNAME' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,LEGALNAME,-1,-1;SURF_TYPE 'SURF_TYPE' true true false 20 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,SURF_TYPE,-1,-1;SPEED 'SPEED' true true false 8 Double 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,SPEED,-1,-1;LCITY 'LCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,LCITY,-1,-1;RCITY 'RCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,RCITY,-1,-1;ONEWAY 'ONEWAY' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,ONEWAY,-1,-1;NAMED 'NAMED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,NAMED,-1,-1;ADDRESSED 'ADDRESSED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,ADDRESSED,-1,-1;NAMELOW 'NAMELOW' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,NAMELOW,-1,-1;SOURCETHM 'SOURCETHM' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,SOURCETHM,-1,-1;LENGTH 'LENGTH' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,LENGTH,-1,-1;COUNTY 'COUNTY' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,COUNTY,-1,-1;REVERSED 'REVERSED' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,REVERSED,-1,-1;BLM 'BLM' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,BLM,-1,-1;USFS 'USFS' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,USFS,-1,-1;MP_DIST 'MP_DIST' true true false 8 Double 4 14 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MP_DIST,-1,-1;MP_BEG 'MP_BEG' true true false 8 Double 4 14 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MP_BEG,-1,-1;MP_END 'MP_END' true true false 8 Double 4 14 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,MP_END,-1,-1;ROADNUMB 'ROADNUMB' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,ROADNUMB,-1,-1;FLIPME 'FLIPME' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,FLIPME,-1,-1;SHAPE_LENG 'SHAPE_LENG' true true false 8 Double 11 19 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,SHAPE_LENG,-1,-1;CROSS1 'CROSS1' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,CROSS1,-1,-1;CROSS2 'CROSS2' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,CROSS2,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.xxxStreets,Shape.len,-1,-1", "")

        # Process: Delete Features (3)...
        arcpy.DeleteFeatures_management(Prod_1_xxx_Streets_Unique)

        # Process: Append (4)...
        arcpy.Append_management("'Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique'", Prod_1_xxx_Streets_Unique, "NO_TEST", "OBJECTID 'OBJECTID' true true false 8 Double 0 10 ,First,#;NAME 'NAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique,NAME,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#,Database Connections\\xxx@xxx-2_prod.sde\\SDE.DBO.Cartegraph\\SDE.DBO.xxx_Streets_Unique,Shape.len,-1,-1", "")

        # Process: Delete Features (4)...
        arcpy.DeleteFeatures_management(Prod_1_xxx_Pavement_Streets)

        # Process: Append (3)...
        arcpy.Append_management("'Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets'", Prod_1_xxx_Pavement_Streets, "NO_TEST", "IDNUM 'IDNUM' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,IDNUM,-1,-1;PREFIX 'PREFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,PREFIX,-1,-1;STREETNAME 'STREETNAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,STREETNAME,-1,-1;STREETTYPE 'STREETTYPE' true true false 4 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,STREETTYPE,-1,-1;SUFFIX 'SUFFIX' true true false 2 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,SUFFIX,-1,-1;CFCC 'CFCC' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,CFCC,-1,-1;CITY_L 'CITY_L' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,CITY_L,-1,-1;CITY_R 'CITY_R' true true false 3 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,CITY_R,-1,-1;FROMLEFT 'FROMLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,FROMLEFT,-1,-1;TOLEFT 'TOLEFT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,TOLEFT,-1,-1;FROMRIGHT 'FROMRIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,FROMRIGHT,-1,-1;TORIGHT 'TORIGHT' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,TORIGHT,-1,-1;ZIP_L 'ZIP_L' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,ZIP_L,-1,-1;ZIP_R 'ZIP_R' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,ZIP_R,-1,-1;POLICE_L 'POLICE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,POLICE_L,-1,-1;POLICE_R 'POLICE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,POLICE_R,-1,-1;FIRE_L 'FIRE_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,FIRE_L,-1,-1;FIRE_R 'FIRE_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,FIRE_R,-1,-1;EMS_L 'EMS_L' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,EMS_L,-1,-1;EMS_R 'EMS_R' true true false 15 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,EMS_R,-1,-1;P_BEAT_L 'P_BEAT_L' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,P_BEAT_L,-1,-1;P_BEAT_R 'P_BEAT_R' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,P_BEAT_R,-1,-1;MAP_PAGE1 'MAP_PAGE1' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE1,-1,-1;MAP_PAGE2 'MAP_PAGE2' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE2,-1,-1;MAP_PAGE3 'MAP_PAGE3' true true false 10 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MAP_PAGE3,-1,-1;X1 'X1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,X1,-1,-1;Y1 'Y1' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,Y1,-1,-1;X2 'X2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,X2,-1,-1;Y2 'Y2' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,Y2,-1,-1;TYPE 'TYPE' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,TYPE,-1,-1;LABELTYPE 'LABELTYPE' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,LABELTYPE,-1,-1;LESN 'LESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,LESN,-1,-1;RESN 'RESN' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,RESN,-1,-1;NAME 'NAME' true true false 30 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,NAME,-1,-1;STREET 'STREET' true true false 72 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,STREET,-1,-1;LEGALNAME 'LEGALNAME' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,LEGALNAME,-1,-1;SURF_TYPE 'SURF_TYPE' true true false 20 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,SURF_TYPE,-1,-1;SPEED 'SPEED' true true false 4 Long 0 10 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,SPEED,-1,-1;LCITY 'LCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,LCITY,-1,-1;RCITY 'RCITY' true true false 32 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,RCITY,-1,-1;ONEWAY 'ONEWAY' true true false 5 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,ONEWAY,-1,-1;NAMED 'NAMED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,NAMED,-1,-1;ADDRESSED 'ADDRESSED' true true false 36 Date 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,ADDRESSED,-1,-1;NAMELOW 'NAMELOW' true true false 36 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,NAMELOW,-1,-1;SOURCETHM 'SOURCETHM' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,SOURCETHM,-1,-1;LENGTH 'LENGTH' true true false 8 Double 0 19 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,LENGTH,-1,-1;COUNTY 'COUNTY' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,COUNTY,-1,-1;REVERSED 'REVERSED' true true false 16 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,REVERSED,-1,-1;BLM 'BLM' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,BLM,-1,-1;USFS 'USFS' true true false 12 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,USFS,-1,-1;MP_DIST 'MP_DIST' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MP_DIST,-1,-1;MP_BEG 'MP_BEG' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MP_BEG,-1,-1;MP_END 'MP_END' true true false 8 Double 4 12 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,MP_END,-1,-1;ROADNUMB 'ROADNUMB' true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,ROADNUMB,-1,-1;FLIPME 'FLIPME' true true false 2 Short 0 5 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,FLIPME,-1,-1;SHAPE_LENG 'SHAPE_LENG' true true false 8 Double 11 18 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,SHAPE_LENG,-1,-1;CROSS2 'CROSS2' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,CROSS2,-1,-1;CROSS1 'CROSS1' true true false 254 Text 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,CROSS1,-1,-1;Shape.len 'Shape.len' false false true 0 Double 0 0 ,First,#,Database Connections\\xxx@xxx-1_prod.sde\\SDE.DBO.xxxStreets,Shape.len,-1,-1", "")

        del arcpy

    except:
        print 'Errors occurred in UpdateStreetsProd1_def'
        raise

    
