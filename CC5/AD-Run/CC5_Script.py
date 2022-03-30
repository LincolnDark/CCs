import csv
import arcpy
import os
arcpy.env.overwriteOutput = True
directory = r"C:\Data\Students_2022\Dark\CC5\AD-Run"
outputDirectory = "Years_Directory"
if not os.path.exists(os.path.join(directory, outputDirectory)):
    os.mkdir(os.path.join(directory, outputDirectory))

# making a list of years
year_list = []
with open(os.path.join(directory, r"CC5_CSV.csv")) as the_csv:
    csv_reader = csv.reader(the_csv)
    line_count = 0
    headerline = next(the_csv)
    for row in csv_reader:
        if row[2] not in year_list:
            year_list.append(row[2])
print(year_list)

# making a csv for each year
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

    # making two shapefiles
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
        print("Good Job, Lincoln!")

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# creating a fishnet for each shapefile
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    outFeatureClass = os.path.join(directory, outputDirectory, str(year) + "_Osprey_nest_locations.shp")
    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
    cellSizeWidth = "0.25"
    cellSizeHeight = "0.25"
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

# joining fishnets to points

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