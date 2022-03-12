# Goals of the tool
# Input a shapefile of all towns in any state, then this tool will tell you
# the names of all the towns, and count the number of towns
# Step 0 - Create a CSV of the attribute table of the shapefile
# Step 1 - create a list of all town names in shapefile
# Step 2 - use a for loop to print the name of each town
# Step 3 - use a for loop to print the number of towns in the dataset

#Step 0
# Changes the user will have to make:

import arcpy
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\Midterm"
arcpy.ExportXYv_stats("towns.shp", "NAME", "COMMA", "Towns.csv",
                      "ADD_FIELD_NAMES")


































