# coding: utf-8
import arcpy
arcpy.env.workspace = "D:\\Users\\admin\\Desktop\\"
arcpy.Select_analysis("ne\\ne.shp", "ne_selected_external.shp", 'NAME = \'Austin\'')
