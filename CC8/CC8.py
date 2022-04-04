# Tool - shrink
# The purpose of this code is (1) to use a function to shrink all forest land cover classes in a dataset, then (2)
# save the layer with shrunken forests. To make this code work on your machine, you will have to enter your own
# workspace into line 11. Also, if you wish to use a different land cover data set, you will have to change line 12 to
# the name of your own file; furthermore, you will have to change line 15 to whichever ObjectIDs the forest land covers
# are classified as in your data set.
# Lincoln Dark - 4Apr22

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC8"
input_raster = r"NLCD_2001.img"

def shrink_and_save_forests(input_raster):
    step_1 = arcpy.sa.Shrink(input_raster, 1, [41,42, 43, 90])
    step_1.save("Shrunken_Forests.img")
    return step_1

shrink_and_save_forests(input_raster)