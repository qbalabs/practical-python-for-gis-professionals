REM Copy and paste below lines from OsGeo4W shell's py3_env command
SET PYTHONPATH=
SET PYTHONHOME=C:\OSGeo4W\apps\Python36
PATH C:\OSGeo4W\apps\Python36;C:\OSGeo4W\apps\Python36\Scripts;C:\OSGeo4W\bin;C:\Windows\system32;C:\Windows;C:\Windows\system32\WBem;C:\OSGeo4W\apps\Python27\Scripts
REM Then change the last path to the output of
REM QgsApplication.prefixPath() from QGIS Plugins->Python Console
REM Replace slashes / with backslashes \ 
SET PYTHONPATH=%PYTHONPATH%;C:\OSGeo4W\apps\qgis\python
python %1

