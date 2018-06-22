r=iface.activeLayer()
print(r.width(), r.height())
print(r.extent().toString())
print(r.rasterType())
print(r.bandCount())
print(r.metadata())

i= r.dataProvider().identify(QgsPointXY(-92.109375,-55.078367), QgsRaster.IdentifyFormatValue)
if i.isValid():
  print(i.results())
