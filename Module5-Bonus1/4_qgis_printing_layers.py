# Printing layers
layers=QgsProject.instance().mapLayers()
for l,lo in layers.items():
    print(l,lo)
    
    