# Lincoln Dark - Coding Challenge 10 - April 18th, 2022
# The first step is importing necessary packages and setting our workspace, so our script knows where to find the data
import arcpy, os
arcpy.env.workspace = r"C:\Users\14017\Desktop\NRS_528\Github\CC10\Landsat_data_lfs\Step_2_data\Winter_2015"

# The next step is to composite the bands we are interested in, in this case, bands 4 & 5.
Composite_Raster = arcpy.CompositeBands_management(in_rasters=
                                                    r"C:\Users\14017\Desktop\NRS_528\Github\CC10\Landsat_data_lfs\
                                                    Step_2_data\Winter_2015\
                                                    LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif;"
                                                    r"C:\Users\14017\Desktop\NRS_528\Github\CC10\Landsat_data_lfs\
                                                    Step_2_data\Winter_2015\
                                                    LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif",
                                out_raster=r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\
                                DataFolder_Step_2_data_lfs\Step_2_data\winter15")

