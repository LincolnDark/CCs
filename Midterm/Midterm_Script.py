# Maybe you are moving to a new state, maybe you are going on vacation to a state that you have never been before, or
# maybe, you just want to learn more about your own state. When planning your journey, your first question is probably
# "how many towns are in this state, and what are all of their names?". Well my friend, fear no longer, as this handy
# Python script will answer all of these questions for you.

# Goals of the tool
# Input a shapefile of all towns in any state, then this tool will tell you
# the names of all the towns, and count the number of towns
# Step 0 - Create a CSV of the attribute table of the shapefile
# Step 1 - use a for loop to print the name of each town
# Step 2 - print the number of towns in the dataset

# Step 0
# Changes the user will have to make:
# line 20- You will have to input your own workspace, because you are not on my machine (hopefully)
# line 22 - You will have to change "towns.shp" to the name of your own towns shapefile

import arcpy

arcpy.env.workspace = r"C:\Data\Students_2022\Dark\Midterm"
arcpy.env.overwriteOutput = True
arcpy.ExportXYv_stats("towns.shp", "NAME", "COMMA", "Towns.csv",
                      "ADD_FIELD_NAMES")

# Step 1
import csv, os
town_list = []
with open("Towns.csv") as Towns_csv:
    headerline = next(Towns_csv)
    for row in csv.reader(Towns_csv):
        if row[2] not in town_list:
            town_list.append(row[2])
print(town_list)

#Step 2
print(len(town_list))

# Congratulations! You now know all the names of all the towns in your input state, and how many there are.
# Enjoy your trip!



































