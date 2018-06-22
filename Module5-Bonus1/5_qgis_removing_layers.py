# Removing one layer at the time
# Printing layers
layers=QgsProject.instance().mapLayers()
lk=list(layers.keys()).pop()
print("Removing:", lk)
QgsProject.instance().removeMapLayer(lk)