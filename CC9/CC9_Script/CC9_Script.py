# Coding Challenge 9 - April 13th 2022 - Lincoln Dark
# Data Prep
import arcpy
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC9"
input_shp = 'RI_Forest_Health_Works_Project%#A_Points_All_Invasives.shp'
fields = ['photo']
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " LIKE  'y%'"
# Part 1 - Counting records with and without photos.
Photo_list = []
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{18}'.format(row[18]))
        count = count + 1

print(count)