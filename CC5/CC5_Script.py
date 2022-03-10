#The Basics
import csv

import arcpy
import csv
import os
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
test = open(str(arcpy.env.workspace + r'\CC5_CSV.csv'), newline='')
testreader = csv.reader(test, delimiter=',')
linecount=0
for row in testreader:
    if row[2] not in years:
        years.append(row[2])
years.pop(0)
print(len(years))
print(years)
#test
# making new CSVs by year
# os.mkdir("Years_Directory")
# header = "lat,long,year"
# for year in years:
#     year_count = 1
#     with open("CC5_CSV.csv") as the_csv:
#         for row in csv.reader(the_csv):
#             if row[0] == year:
#                 file = open(r"Years_Directory/" + str(year) + ".csv", "w")
#                 file.write(header)
#                 year_count = 0
#     file.close()


for year in years:
    with open('%s-output.csv' % year, 'w', newline='') as next_csv:
        csv_creator = csv.writer(next_csv)
        csv_creator.writerow(['lat', 'long', 'year'])
        for row in testreader:
            if row[2] == year:
                csv_creator.writerow(row[0])


# with open(arcpy.env.workspace + r'\CC5_CSV.csv') as the_csv:
#     headerline = the_csv.next()
#     for row in csv.reader(the_csv):
#         if row[0] not in years:
#             years.append(row[0])
# print(len(years))
# os.mkdir("Years_Directory")
# header = "lat,long,year"
# years = [2010,2020]
# # for year in years:
# #     year_list = 1
# #     with open("CC5_CSV.csv") as Table:
# #         for row in csv.reader(Table):
# #             if row[0] == year:
# #                 if year_list == 1:
# #                     file = open(r"Years_Directory/" + str(year) + ".csv", "w")
# #                     file.write(header)
# #                     year_list = 0
# #     file.close()
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