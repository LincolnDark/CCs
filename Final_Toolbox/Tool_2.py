# Lincoln Dark - April 20th, 2022 - NRS 528 - Final Toolbox Tool 2
# The purpose of this tool is to prepare the wetlands and roads data for the suitability analysis in tool 3.
# Tool 2 is split into 2 parts; tool 2a and tool 2b. Tool 2a prepares the wetlands data, while tool 2b prepares the
# roads data.

# The first step is to prepare set our working directory, import necessary packages, and define the variables.
import arcpy
from arcpy.sa import *
working_directory = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data"
arcpy.env.workspace = working_directory
Wetlands = "wetlands.shp"
Roads = "roads.shp"
Study_area = "study_area.shp"
arcpy.env.overwriteOutput = True

# Tool 2a
arcpy.analysis.Select(Wetlands, "Forested_Wetlands.shp", "WETLAND_TY='Freshwater Forested/Shrub Wetland'")
arcpy.Clip_analysis("Forested_Wetlands.shp", Study_area, "FW_in_SA.shp")
arcpy.FeatureToRaster_conversion("FW_in_SA.shp", "ACRES", "FW_in_SA_RAS.tif", 10)
arcpy.ddd.Int("FW_in_SA_RAS.tif", "FW_in_SA_Int")
RegionGroup("FW_in_SA_Int", "EIGHT", "", "", "")
Reclassify("FW_in_SA_Int", "COUNT", RemapRange([[0,5380,"NODATA"],[5380, 10760,"1"],[10760,64580,"2"],[64580,100000000000,"3"]]))
