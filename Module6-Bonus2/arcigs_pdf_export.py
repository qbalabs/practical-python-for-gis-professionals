# coding: utf-8
# Get the current project
p=arcpy.mp.ArcGISProject('CURRENT')

# And the first map from the project
m=p.listMaps()[0]

# And the main view that is ready for print
m.defaultView

# Then just export it to a PDF file
m.defaultView.exportToPDF('D:\\Users\\admin\\Desktop\test.pdf', 800, 600)
