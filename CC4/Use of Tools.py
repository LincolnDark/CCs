# Tool - shrink
# The purpose of this code is to shrink all deciduous forest areas by 1 pixel.
# Lincoln Dark - March 2022

import arcpy

arcpy.env.workspace = "C:\Data\Students_2022\Dark\CC4"
Outshrink = arcpy.sa.Shrink("NLCD_2001.img", 1, [6])
Outshrink.save("NLCD_2001_shrink.img")


