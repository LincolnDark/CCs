# First, we must import packages that we will need for our code to function, as well as set up the directories to tell
# our code where to pull files from as well as store files that we will create.
import csv
import arcpy
import os
arcpy.env.overwriteOutput = True
directory = r"C:\Users\14017\Desktop\NRS_528\Github\CC5"
outputDirectory = "Years_Directory"
if not os.path.exists(os.path.join(directory, outputDirectory)):
    os.mkdir(os.path.join(directory, outputDirectory))

# Second, we will make a list of years using our CSV full of data. This will allow us to make two seperate CSVs, 1 for
# each year, in the next step.
year_list = []
with open(os.path.join(directory, r"CC5_CSV.csv")) as the_csv:
    csv_reader = csv.reader(the_csv)
    line_count = 0
    headerline = next(the_csv)
    for row in csv_reader:
        if row[2] not in year_list:
            year_list.append(row[2])
print(year_list)

# Using our list of unique years, we will make two seperate CSVs, one for each year. Doing this will allow us to
# create a shapefile for each year in the next step.
for year in year_list:
    with open(os.path.join(directory, r"CC5_CSV.csv")) as the_csv:
        csv_reader = csv.reader(the_csv)
        file = open(os.path.join(directory, outputDirectory, str(year) + ".csv"), "w")
        file.write(headerline)
        for row in csv_reader:
            if row[2] == year:
                file.write(",".join(row))
                file.write("\n")
        file.close()

    # Now that we have a CSV for each year, we can use each CSV to make a shapefile for the data that is associated
    # with that year.
    in_Table = os.path.join(directory, outputDirectory, str(year) + ".csv")
    x = "long"
    y = "lat"
    z_coords = ""
    out_Layer = "years"
    saved_Layer = os.path.join(directory, outputDirectory, str(year) + "Osprey_map.shp")
    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x, y, out_Layer, spRef, z_coords)
    print(arcpy.GetCount_management(out_Layer))
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print("The shapefile exists!")

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# This code will create a fishnet for the points in each shapefile. Making a fishnet will allow us to create our
# heatmap, which visualizes the density of points in a gridcell of the fishnet.
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    outFeatureClass = os.path.join(directory, outputDirectory, str(year) + "_Osprey_nest_locations.shp")
    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
    cellSizeWidth = "0.125"
    cellSizeHeight = "0.125"
    numRows = ""
    numColumns = ""
    oppositeCorner = str(XMax) + " " + str(YMax)
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"
    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
    if arcpy.Exists(outFeatureClass):
        print("Created " +str(year) + " fishnets!")

# In this step, we join the points from each layer to their fishnet. This places the fishnet in the correct place
# on the map.

    target_features = os.path.join(directory, outputDirectory, str(year) + "_Osprey_nest_locations.shp")
    join_features = os.path.join(directory, outputDirectory, str(year) + "Osprey_map.shp")
    out_feature_class = os.path.join(directory, outputDirectory, str(year) + "_heatmap.shp")
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

    if arcpy.Exists(outFeatureClass):
        print("Created " +str(year) + " heatmap!")
        print("Deleting unneccessary files")
        arcpy.Delete_management(target_features)
        arcpy.Delete_management(join_features)