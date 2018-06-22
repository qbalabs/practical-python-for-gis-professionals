# Working with selected features
# GUI vs. script
l=iface.activeLayer()
# Clean up previous selection
l.removeSelection()
bbox=QgsRectangle(-92.109375,-55.078367,-37.089844,14.774883)
request = QgsFeatureRequest().setFilterRect(bbox)
features=l.getFeatures(request)
# Create list of feature ids for selection
fids=[]
for f in features:
    fid=f.id()
    print(fid)
    fids.append(fid)
print(fids)
l.select(fids)

# Once we've selected features 
# wen can also go over them
for f in l.selectedFeatures():
    print(f)