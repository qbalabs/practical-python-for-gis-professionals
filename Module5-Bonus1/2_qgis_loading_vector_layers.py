# This layer will be loaded and visible in QGIS straight away
l1=iface.addVectorLayer('D:/Users/admin/Desktop/ne_10m_populated_places_simple/ne_10m_populated_places_simple.shp','new_layer1','ogr')
if not l1:
    print('Failed to load layer!')
else:
    print(l1)