# Lincoln Dark - NRS 528 - Coding Challenge 7
# This code generate heatmaps that can be used in GIS of the distribution of
# Osprey nests in both the years 2010 and 2020.

import csv
import arcpy
import os
import glob
arcpy.env.overwriteOutput = True
directory = r"C:\Users\14017\Desktop\NRS_528\Github\CC7"
output_Directory = "Years_Directory"
data_file = "CC5_CSV.csv"


if not os.path.exists(os.path.join(directory, output_Directory)):
    os.mkdir(os.path.join(directory, output_Directory))
if not os.path.exists(os.path.join(directory, "output_files")):
    os.mkdir(os.path.join(directory, "output_files"))
if not os.path.exists(os.path.join(directory, "temporary_files")):
    os.mkdir(os.path.join(directory, "temporary_files"))

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

year_list = []
with open(os.path.join(directory, data_file)) as year_csv:
    header_line = next(year_csv)
    for row in csv.reader(year_csv):
        try: #Using try/except saves us if there is a line with no data in the file
            if row[2] not in year_list:
                year_list.append(row[2])
        except:
            pass

# making a csv for each year
for year in year_list:
    with open(os.path.join(directory, r"CC5_CSV.csv")) as the_csv:
        csv_reader = csv.reader(the_csv)
        file = open(os.path.join(directory, output_Directory, str(year) + ".csv"), "w")
        file.write(headerline)
        for row in csv_reader:
            if row[2] == year:
                file.write(",".join(row))
                file.write("\n")
        file.close()


# splitting the files

if len(year_list) > 1:
    for year in year_list:
        year_count = 1
        with open(os.path.join(directory, data_file)) as year_csv:
            header = next(year_csv)
            for row in csv.reader(year_csv):
                if row[2] == year:
                    if year_count == 1:
                        file = open(
                            os.path.join(directory, "temporary_files", str(year.replace(" ", "_")) + ".csv"),
                            "w")
                        file.write(header)
                        year_count = 0
                    # make well formatted line
                    file.write(",".join(row))
                    file.write("\n")
        file.close()

# making two shapefiles

os.chdir(os.path.join(directory, "temporary_files"))  # same as env.workspace
arcpy.env.workspace = os.path.join(directory, "output_files")
year_file_list = glob.glob("*.csv")  # Find all CSV files

count = 0

for year_file in year_file_list:
    print(".. Processing: " + str(year_file) + " by converting to shapefile format")
    in_Table = year_file
    x_coords = "lat"
    y_coords = "long"
    z_coords = ""
    out_Layer = "year" + str(count)
    saved_Layer = year_file.replace(".", "_") + ".shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
arcpy.CopyFeatures_management(lyr, saved_Layer)
count = count + 1
arcpy.Delete_management(lyr)

in_Table = os.path.join(directory, output_Directory, str(year) + ".csv")
x = "long"
y = "lat"
z_coords = ""
out_Layer = "years"
saved_Layer = os.path.join(directory, output_Directory, str(year) + "Osprey_map.shp")
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x, y, out_Layer, spRef, z_coords)
print(arcpy.GetCount_management(out_Layer))
arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print("Layer has been saved")

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# creating a fishnet for each shapefile
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    outFeatureClass = os.path.join(directory, output_Directory, str(year) + "_Osprey_nest_locations.shp")
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

    target_features = os.path.join(directory, output_Directory, str(year) + "_Osprey_nest_locations.shp")
    join_features = os.path.join(directory, output_Directory, str(year) + "Osprey_map.shp")
    out_feature_class = os.path.join(directory, output_Directory, str(year) + "_heatmap.shp")
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

arcpy.Delete_management(os.path.join(directory, "temporary_files"))