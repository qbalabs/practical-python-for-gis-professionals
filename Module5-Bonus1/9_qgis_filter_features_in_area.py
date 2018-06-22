# Getting features from bbox
l=iface.activeLayer()
bbox=QgsRectangle(-92.109375,-55.078367,-37.089844,14.774883)
request = QgsFeatureRequest().setFilterRect(bbox)
features=l.getFeatures(request)
print('Found', len(list(features)), 'features in a given area')