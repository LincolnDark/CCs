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

# os.rmdir("Years_Directory")


# arcpy.env.overwriteOutput = True
# lyr = arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, out_layer, spRef)
# arcpy.CopyFeatures_management(lyr, saved_layer)
# if arcpy.Exists(saved_layer):
#     print("Created file successfully!")
# #Querying distribution by year (As my CSV is comprised of two seperate years of Osprey distribution)
# Years_2010 = arcpy.SelectLayerByAttribute_management("osprey_polygon.shp", "NEW_SELECTION", "year = 2010")
#
# #Extracting Extent
# desc = arcpy.Describe(saved_layer)
# XMin = desc.extent.XMin
# XMax = desc.extent.XMax
# YMin = desc.extent.YMin
# YMax = desc.extent.YMax