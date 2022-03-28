import csv
import arcpy
import os
arcpy.env.overwriteOutput = True
directory = r"C:\Users\14017\Desktop\NRS_528\Github\CC5"
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

# making a shapefile
    # in_Table = os.path.join(directory, outputDirectory, str(year) + ".csv")
    # x = "long"
    # y = "lat"
    # z_coords = ""
    # out_Layer = "years"
    # saved_Layer = os.path.join(directory, outputDirectory, str(year) + "Osprey_map.shp")
    # spRef = arcpy.SpatialReference(4326)
    # lyr = arcpy.MakeXYEventLayer_management(in_Table, x, y, out_Layer, spRef, z_coords)
    # print(arcpy.GetCount_management(out_Layer))
    # arcpy.CopyFeatures_management(lyr, saved_Layer)
    # if arcpy.Exists(saved_Layer):
    #     print("Good Job, Lincoln!")
    #
    # desc = arcpy.Describe(saved_Layer)
    # XMin = desc.extent.XMin
    # XMax = desc.extent.XMax
    # YMin = desc.extent.YMin
    # YMax = desc.extent.YMax

