# Getting features using expression
l=iface.activeLayer()
qe=QgsExpression("name ILIKE '%town%'")
request = QgsFeatureRequest(qe)
features=l.getFeatures(request)
print('Found', len(list(features)), 'features that match expression')