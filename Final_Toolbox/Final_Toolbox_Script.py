import arcpy
arcpy.env.overwriteOutput = True
params = []
Towns = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\towns.shp"
Coast = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\Coastline.shp"
Wetlands = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\Wetlands.shp"
Tool1_Output = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Buffered_Coastline.shp"
Tool2_Output = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Forested_Wetlands.shp"

class Toolbox(object): # This block of code defines the toolbox
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Final Python Toolbox"
        self.alias = ""


        self.tools = [Tool1, Tool2, Tool3]

class Tool1(object): # Defining the first tool
    def __init__(self):
        self.label = "Buffering Coastline"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        # This block will define parameter information
        params = []
        input_poly1 = arcpy.Parameter(name="input_poly1",
                                     displayName="Input Polygon",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        input_poly1.value = Coast
        params.append(input_poly1)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = Tool1_Output
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_poly1 = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.Buffer_analysis(in_features=input_poly1,
                              out_feature_class=Tool1_Output,
                              buffer_distance_or_field="5 miles")
        return

class Tool2(object):
    def __init__(self):
        self.label = "Defining Forested Wetlands"
        self.description = ""
        self.canRunInBackground = False
    def getParameterInfo(self):
        # This block will define parameter information
        params = []
        input_poly2 = arcpy.Parameter(name="input_poly2",
                                     displayName="Input Polygon",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        input_poly2.value = Wetlands
        params.append(input_poly2)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = Tool2_Output
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_poly1 = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.SelectLayerByAttribute_management(in_features=input_poly2,
                                                out_feature_class=Tool2_Output,
                                                where_clause="WETLAND_TY='Freshwater Forested/Shrub Wetland'")
        return

    