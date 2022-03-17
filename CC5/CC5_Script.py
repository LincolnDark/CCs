#The Basics
import csv
import arcpy

arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC5"
in_table = r"CC5_CSV.csv"
x_coords = "lat"
y_coords = "long"
out_layer = "osprey"
saved_layer = r"osprey_polygon.shp"
#Creating the Shapefile based on the .csv
spRef = arcpy.SpatialReference(4326)
#extracting by unique year
years = []
with open(in_table) as the_csv:
    headerline = next(the_csv)
    for row in csv.reader(the_csv):
        if row[2] not in years:
            years.append(row[2])
print(len(years))
print(years)

#Use countries example as guide

# making new CSVs by year
import os
outputDirectory = "Years_Directory"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)
for year in years:
    with open("CC5_CSV.csv") as the_csv:
        file = open(os.path.join(outputDirectory, str(year) + ".csv"), "w")
        file.write(headerline)
        for row in csv.reader(the_csv):
            if row[2] == year:
                file.write(",".join(row))
                file.write("\n")

# making the shapefiles
# arcpy.env.overwriteOutput = True
# for year in years:
# See line 44, what do I put in for the 1st and 4th input? I don't know how to code this so I get two seperate
# files, one for 2010 and one for 2020.

# lyr_2010 = arcpy.MakeXYEventLayer_management(r"2010.csv", "long", "lat", "Osprey_2010", spRef)
# arcpy.CopyFeatures_management(lyr_2010, r"Osprey_2010.shp")
# if arcpy.Exists(r"Osprey_2010.shp"):
#     print("Good Job Lincoln!")

# lyr_2020 = arcpy.MakeXYEventLayer_management(r"2020.csv", "long", "lat", "Osprey_2020", spRef)
# arcpy.CopyFeatures_management(lyr_2020, r"Osprey_2020.shp")
# if arcpy.Exists(r"Osprey_2020.shp"):
#     print("Good Job Lincoln, you did it twice!")

# describing the shapefiles
# desc = arcpy.Describe("Osprey_2010.shp")
# XMin = desc.extent.XMin
# XMax = desc.extent.XMax
# YMin = desc.extent.YMin
# YMax = desc.extent.YMax
# print(XMin, XMax, YMin, YMax)
#
# # Fishnet
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
# outFeatureClass_2010 = "Fishnet_2010.shp"
# originCoordinate = str(XMin) + " " + str(YMin)  # Left bottom of our point data
# yAxisCoordinate = str(XMin) + " " + str(YMin + 1)  # This sets the orientation on the y-axis, so we head north
# cellSizeWidth = "0.25"
# cellSizeHeight = "0.25"
# numRows = ""  # Leave blank, as we have set cellSize
# numColumns = "" # Leave blank, as we have set cellSize
# oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
# labels = "NO_LABELS"
# templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
# geometryType = "POLYGON"  # Create a polygon, could be POLYLINE
#
# arcpy.CreateFishnet_management(outFeatureClass_2010, originCoordinate, yAxisCoordinate,
#                                cellSizeWidth, cellSizeHeight, numRows, numColumns,
#                                oppositeCorner, labels, templateExtent, geometryType)
#
# if arcpy.Exists(outFeatureClass_2010):
#     print("Created 2010 Fishnet file successfully!")
#
# # Spatially join the fishnet to the shapefile
# target_features="Fishnet_2010.shp"
# join_features="Osprey_2010.shp"
# out_feature_class="HeatMap_2010.shp"
# join_operation="JOIN_ONE_TO_ONE"
# join_type="KEEP_ALL"
# field_mapping=""
# match_option="INTERSECT"
# search_radius=""
# distance_field_name=""
#
# arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
#                            join_operation, join_type, field_mapping, match_option,
#                            search_radius, distance_field_name)
# # check if it works
# if arcpy.Exists(out_feature_class):
#     print("Created Heatmap file successfully!")
#     print("Deleting intermediate files")