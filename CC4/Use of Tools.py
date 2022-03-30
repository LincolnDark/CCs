# Tool - shrink
# The purpose of this code is to shrink all forest areas (deciduous, evergreen, mixed, and woody wetlands) by 1 pixel.
# Lincoln Dark - March 2022

import arcpy

def Model():
    arcpy.env.overwriteOutput = False
    arcpy.CheckOutExtension("spatial")
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\14017\Documents\ArcGIS\Projects\FixingCC4\FixingCC4.gdb", workspace=r"C:\Users\14017\Documents\ArcGIS\Projects\FixingCC4\FixingCC4.gdb"):
        NLCD_2001_img = arcpy.Raster("NLCD_2001.img")
        Shrink_NLCD_1 = "C:\\Users\\14017\\Documents\\ArcGIS\\Projects\\FixingCC4\\FixingCC4.gdb\\Shrink_NLCD_1"
        Shrink = Shrink_NLCD_1
        with arcpy.EnvManager(scratchWorkspace=r"C:\Users\14017\Documents\ArcGIS\Projects\FixingCC4\FixingCC4.gdb", workspace=r"C:\Users\14017\Documents\ArcGIS\Projects\FixingCC4\FixingCC4.gdb"):
            Shrink_NLCD_1 = arcpy.sa.Shrink(in_raster=NLCD_2001_img, number_cells=1, zone_values=[41, 42, 43, 90], shrink_method="MORPHOLOGICAL")
            Shrink_NLCD_1.save(Shrink)


if __name__ == '__main__':
    Model()

# code generated using ArcGIS Pro Modelbuilder