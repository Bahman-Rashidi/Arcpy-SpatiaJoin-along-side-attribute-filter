# Arcpy-SpatiaJoin-along-side-attribute-filter
doing attribute filter on 2 layer  and ne  to spatial join on result base on the  INTERSECTS  
1-add srcript to a connection

2-copy  your connection to  this  folder  or  any  address "C:\\data\\WEBGISCNN.sde"

3-add this  parameters to  the script
 
layerName1 = arcpy.GetParameter(0) -

Query1 = arcpy.GetParameter(1)-

layerName2 = arcpy.GetParameter(2)-

Query2 = arcpy.GetParameter(3)-

match_option = arcpy.GetParameter(4)-

join_type = arcpy.GetParameter(5)-

join_operation = arcpy.GetParameter(6)-


user = arcpy.GetParameter(7)-
databse = arcpy.GetParameter(8)-
connectionname = arcpy.GetParameter(9)-
SearchRadius = arcpy.GetParameter(10)-

4-remeber  to  add  a parameter  as  output for result

5-save it

6-run the script  and next  fill al paramer 

7-you must get  only  Ids  of  first layer  (OBEJCTID)

8-share  result  on the  web  and  now  you can  use the  webservice  for doing  spatial join
