# Filtering features
l=iface.activeLayer()
# Get only 4 first features
request = QgsFeatureRequest().setLimit(4)
for f in l.getFeatures(request):
    print(f['name'])