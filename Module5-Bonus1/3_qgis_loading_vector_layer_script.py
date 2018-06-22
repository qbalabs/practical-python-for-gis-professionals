# This layer will be loaded,but become visible only 
# when we added it to the layer's registry
# you will use this method in scripts when you don't need to show
# layer in the GUI
l2=QgsVectorLayer('D:/Users/admin/Desktop/ne_10m_populated_places_simple/ne_10m_populated_places_simple.shp','new_layer1','ogr')
print(l2)
if l2.isValid():
    QgsProject.instance().addMapLayer(l2)
else:
    print('Problem loading layer')
