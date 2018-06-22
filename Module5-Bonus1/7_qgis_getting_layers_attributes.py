# Available attributes
l=iface.activeLayer()
for attr in l.fields():
    print('Attr', attr.name(), attr.typeName())