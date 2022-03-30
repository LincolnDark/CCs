# Tool - shrink
# The purpose of this code is to shrink all forest areas (deciduous, evergreen, mixed, and woody wetlands) by 1 pixel.
# Lincoln Dark - March 2022

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC4"
Outshrink = arcpy.sa.Shrink("NLCD_2001.img", 1, [41,42, 43, 90])
Outshrink.save("NLCD_2001_shrink.img")


