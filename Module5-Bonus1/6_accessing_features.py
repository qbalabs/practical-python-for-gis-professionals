# Getting features
l=iface.activeLayer()
nf=l.featureCount()
print("Number of features:", nf)
# This will probably take a lot of time
# Hit ctrl-c in Python console to stop it
for f in l.getFeatures():
    print(f.id(), f.geometry(), f.attributes())
    print("Accessing specific attribute of a feature 'name'", f['name'])
    # Stop after printing the first feature
    if True:
        break
