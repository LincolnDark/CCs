# Coding Challenge 9 - April 13th 2022 - Lincoln Dark
# Data Prep
import arcpy
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC9"
input_shp = 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
fields = ['photo']
# Part 1 - Counting records with and without photos.
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " LIKE  'y%'" # This queries all rows in the photo field
# that have a value of "y", indicating that they have photos.
count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        count = count + 1
print(count)

NoPhotos = arcpy.AddFieldDelimiters(input_shp, "photo") + " LIKE '%'" # This queries all rows in the photo field.
count1 = 0
with arcpy.da.SearchCursor(input_shp, fields, NoPhotos) as cursor:
    for row in cursor:
        count1 = count1 + 1
print(count1 - count) # This line substracts the number of rows with photos from the overall number, telling us the
# number of rows that do not have photos.

