import arcpy
arcpy.env.overwriteOutput = True
params = []
Towns = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\towns.shp"



Tool3_Output = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Coastal_Forested_Wetlands.shp"

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
        input_poly1.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\Coastline.shp"
        params.append(input_poly1)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Buffered_Coastline.shp"
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
                              out_feature_class=output,
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
        input_poly2.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Final_Tool_Data\Wetlands.shp"
        params.append(input_poly2)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Forested_Wetlands.shp"
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
        input_poly2 = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.Select_analysis(in_features=input_poly2,
                              out_feature_class=output,
                              where_clause="WETLAND_TY='Freshwater Forested/Shrub Wetland'")
        return

class Tool3(object):
    def __init__(self):
        self.label = "Clipping Wetlands to Study Area"
        self.description = ""
        self.canRunInBackground = False
    def getParameterInfo(self):
        # This block will define parameter information
        params = []
        input_poly3 = arcpy.Parameter(name="input_poly3",
                                      displayName="Input Polygon",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Input")
        input_poly3.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Buffered_Coastline.shp"
        params.append(input_poly3)

        input_poly4 = arcpy.Parameter(name="input_poly4",
                                     displayName="Input Polygon",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")
        input_poly4.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Forested_Wetlands.shp"
        params.append(input_poly4)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output")
        output.value = r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Coastal_Forested_Wetlands.shp"
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
        input_poly3 = parameters[0].valueAsText
        input_poly4 = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Forested_Wetlands.shp",
                            clip_features=r"C:\Users\14017\Desktop\NRS_528\Github\Final_Toolbox\Buffered_Coastline.shp",
                            out_feature_class=output,
                            cluster_tolerance="")

        return