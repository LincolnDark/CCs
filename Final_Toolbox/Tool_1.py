# Lincoln Dark - April 20th, 2022 - NRS 528 - Final Toolbox Tool 1
# The purpose of this tool is to define the study area, this will select all areas that are 10 miles
# or greater from the coastline.

# First, we must import necessary packages set our working directory, define the working directory to your own
# directory and the Coastline and Towns variables to the data you wish to use.
import arcpy
from arcpy.sa import *
working_directory = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data"
arcpy.env.workspace = working_directory
Coastline = "Coastline.shp"
Towns = "towns.shp"

# Apply a 10-mile buffer to the coastline
arcpy.analysis.Buffer(Coastline, "Buffered_coastline.shp", "10 miles")

# Remove areas where the buffered coastline overlaps with your state / province. The Erase tool is used because we want
# to remove all areas within the coastline buffer
arcpy.analysis.Erase("towns.shp", "Buffered_coastline.shp", "study_area.shp")

# Now that our study area has been defined, we can move to the second tool of the toolbox