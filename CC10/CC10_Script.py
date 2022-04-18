# Lincoln Dark - Coding Challenge 10 - April 18th, 2022
# The first step is importing necessary packages and setting our workspace, so our script knows where to find the data
# To make this code work on your own machine, change working_directory to where your data is stored, and change
# output_directory to where you would like the final NDVI rasters to be saved to.
import arcpy, os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
working_directory = r"C:\Users\14017\Desktop\NRS_528\CC10_Data"
arcpy.env.workspace = working_directory
output_directory = r"C:\Users\14017\Desktop\NRS_528\Github\CC10"

# This section assigns a name to each of our rasters
Feb_B4 = arcpy.Raster(os.path.join(working_directory, "201502", "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif"))
Feb_B5 = arcpy.Raster(os.path.join(working_directory, "201502", "LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif"))
Apr_B4 = arcpy.Raster(os.path.join(working_directory, "201504", "LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif"))
Apr_B5 = arcpy.Raster(os.path.join(working_directory, "201504", "LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif"))
May_B4 = arcpy.Raster(os.path.join(working_directory, "201505", "LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif"))
May_B5 = arcpy.Raster(os.path.join(working_directory, "201505", "LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif"))
Jul_B4 = arcpy.Raster(os.path.join(working_directory, "201507", "LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif"))
Jul_B5 = arcpy.Raster(os.path.join(working_directory, "201507", "LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif"))
Oct_B4 = arcpy.Raster(os.path.join(working_directory, "201510", "LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif"))
Oct_B5 = arcpy.Raster(os.path.join(working_directory, "201510", "LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif"))
Nov_B4 = arcpy.Raster(os.path.join(working_directory, "201511", "LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif"))
Nov_B5 = arcpy.Raster(os.path.join(working_directory, "201511", "LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif"))


Feb_NVDI = RasterCalculator([Feb_B4, Feb_B5], ["x", "y"], "(y-x)/(y+x)") #This line uses the raster calculator tool
# from ArcGIS pro to conduct the NVDI equation on our rasters
Feb_NVDI.save(output_directory + "\Feb_NVDI") # This line saves the NVDI raster for February to our output directory
Apr_NVDI = RasterCalculator([Apr_B4, Apr_B5], ["x", "y"], "(y-x)/(y+x)")
Apr_NVDI.save(output_directory + "\Apr_NVDI")
May_NVDI = RasterCalculator([May_B4, May_B5], ["x", "y"], "(y-x)/(y+x)")
May_NVDI.save(output_directory + "\May_NVDI")
Jul_NVDI = RasterCalculator([Jul_B4, Jul_B5], ["x", "y"], "(y-x)/(y+x)")
Jul_NVDI.save(output_directory + "\Jul_NVDI")
Oct_NVDI = RasterCalculator([Oct_B4, Oct_B5], ["x", "y"], "(y-x)/(y+x)")
Oct_NVDI.save(output_directory + "\Oct_NVDI")
Nov_NVDI = RasterCalculator([Nov_B4, Nov_B5], ["x", "y"], "(y-x)/(y+x)")
Nov_NVDI.save(output_directory + "\\Nov_NVDI")










