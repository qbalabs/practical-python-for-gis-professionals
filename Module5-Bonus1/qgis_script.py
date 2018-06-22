from qgis.core import *

# Change the first argument to your QGIS installation path
# you can get it by going to Plugins->Python Console in QGIS
# and call QgsApplication.prefixPath().
QgsApplication.setPrefixPath("C:/OSGeo4W/apps/qgis", True)

qgs = QgsApplication([], False)
qgs.initQgis()

# You can write your code here
print('Hello qgis world')
print(QgsVectorLayer)
    
# When you're done call the following to clean up
qgs.exitQgis()

