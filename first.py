__author__ = 'Administrator'
import arcpy
from arcpy import env

arcpy.env.workspace = "D:\GP IDW"
dbs = arcpy.ListFeatureClasses()
for db in dbs:
    print(db)
    desc = arcpy.Describe(db)
    print(desc.shapeType)



print(env.workspace)