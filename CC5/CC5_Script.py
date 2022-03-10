#The Basics
import arcpy
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Class_05"
in_table = r"CC5_CSV.csv"
x_coords = "lat"
y_coords = "long"
out_layer = "osprey"
saved_layer = "osprey_polygon.shp"
#Creating the Shapefile based on the .csv
spRef = arcpy.SpatialReference(4326)
arcpy.env.overwriteOutput = True
lyr = arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, out_layer, spRef)
arcpy.CopyFeatures_management(lyr, saved_layer)
if arcpy.Exists(saved_layer):
    print("Created file successfully!")
#Querying distribution by year (As my CSV is comprised of two seperate years of Osprey distribution)
Years_2010 = arcpy.SelectLayerByAttribute_management("osprey_polygon.shp", "NEW_SELECTION", "'year' = 2010")


#Extracting Extent
# desc = arcpy.Describe(saved_layer)
# XMin = desc.extent.XMin
# XMax = desc.extent.XMax
# YMin = desc.extent.YMin
# YMax = desc.extent.YMax