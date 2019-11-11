import arceditor
import sys
import arcpy
import arcpy.mapping as mapping
import base64
import uuid
import datetime
import json  
import numpy as np
arcpy.env.workspace = "C:\\data\\WEBGISCNN.sde"

currentDateTime = datetime.datetime.now()
spal = None
arcpy.AddMessage("  {} ".format("input In Script  ID name"))
layerName1 = arcpy.GetParameter(0)
Query1 = arcpy.GetParameter(1)

layerName2 = arcpy.GetParameter(2)
Query2 = arcpy.GetParameter(3)
match_option = arcpy.GetParameter(4)
join_type = arcpy.GetParameter(5)
join_operation = arcpy.GetParameter(6)

user = arcpy.GetParameter(7)
databse = arcpy.GetParameter(8)
connectionname = arcpy.GetParameter(9)
SearchRadius = arcpy.GetParameter(10)



TargetObjIds = ""

memoryFeature1 = "in_memory" + "\\" + "myMemoryFeature1"
memoryFeature2 = "in_memory" + "\\" + "myMemoryFeature2"
spatial_reference = arcpy.SpatialReference('Projected Coordinate Systems/World/WGS 1984 Web Mercator (auxiliary sphere)')
arcpy.env.workspace = "C:\\data\\" + connectionname
sdeaddress = "C:\\Users\\" + user + "\\AppData\\Roaming\\Esri\\Desktop10.2\\ArcCatalog\\" + connectionname+"\\"+ databse + ".SDE.elec"

fullPath1=sdeaddress + "\\" + layerName1
fullPath2=sdeaddress + "\\" + layerName2

def get_a_uuid():

    return str(uuid.uuid4())
MtGuid = get_a_uuid()

desc1 = arcpy.Describe(fullPath1)
desc2 = arcpy.Describe(fullPath2)

FC1 = arcpy.CreateFeatureclass_management("in_memory","fc1q",desc1.shapeType,"","DISABLED","DISABLED",spatial_reference)
for FeatureClass in FC1:
                        arcpy.AddField_management(FeatureClass, "TableName", "TEXT", "", "", "80", "", "NULLABLE", "NON_REQUIRED", "")
                        arcpy.AddField_management(FeatureClass, "Obj_ID", "TEXT", "", "", "80", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddMessage(" FC1 created")
FC2 = arcpy.CreateFeatureclass_management("in_memory","fc2q",desc2.shapeType,"","DISABLED","DISABLED",spatial_reference)
for FeatureClass in FC2:
                        arcpy.AddField_management(FeatureClass, "TableName", "TEXT", "", "", "80", "", "NULLABLE", "NON_REQUIRED", "")
                        arcpy.AddField_management(FeatureClass, "Obj_ID", "TEXT", "", "", "80", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddMessage(" FC2 created")

FCResult = arcpy.CreateFeatureclass_management("in_memory","fcresult",desc1.shapeType,"","DISABLED","DISABLED",spatial_reference)


arcpy.AddMessage(" Add CreateFeatureclases ")

with arcpy.da.SearchCursor(fullPath1,("OBJECTID","SHAPE@","SHAPE@JSON"),Query1, spatial_reference=spatial_reference)as cursora1:
     with arcpy.da.InsertCursor(FC1,("OID","Shape","TableName","Obj_ID",)) as iCur:
          for row in cursora1:
                     iCur.insertRow((row[0],row[1],layerName1,row[0]))

with arcpy.da.SearchCursor(fullPath2,("OBJECTID","SHAPE@","SHAPE@JSON"),Query2, spatial_reference=spatial_reference)as cursora2:
     with arcpy.da.InsertCursor(FC2,("OID","Shape","TableName","Obj_ID",)) as iCur:
          for row in cursora2:
                     iCur.insertRow((row[0],row[1],layerName2,row[0]))


fieldmappings = arcpy.FieldMappings()

fieldmappings.addTable(FCResult)

outfc = "in_memory\\outresult4"

arcpy.SpatialJoin_analysis(FC1,FC2,outfc,"JOIN_ONE_TO_ONE","KEEP_ALL","#","INTERSECTS",SearchRadius)
arcpy.AddMessage(" SpatialJoin_analysis created")
with arcpy.da.SearchCursor(outfc,["Obj_ID"])as DistCursor:
     for rowa in DistCursor:
         arcpy.AddMessage(str(rowa[0]))
         TargetObjIds = TargetObjIds + str(rowa[0]) + ","
arcpy.AddMessage("TargetObjIds = "+TargetObjIds)
arcpy.SetParameter(11,TargetObjIds) 

                                                

