######
#TRANFORMACION DE MAPAS DEL FORMATO NETCDF A RASTERS GEOTIFF
######

# Import system modules  (Importa ArcGis)
import os
import arcpy
from arcpy import env

arcpy.CheckOutExtension("Spatial")

'''Precipitation Difference'''
env.workspace = r"Y:/ECMWF_Runoff/Difference/yearly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
mean = arcpy.sa.Raster(mean) * 1000
mean.save(r"Y:/ECMWF_Runoff/Difference/annual/diff_total_y.tif")

env.workspace = r"Y:/ECMWF_Runoff/Difference/monthly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
mean = arcpy.sa.Raster(mean) * 1000
mean.save(r"Y:/ECMWF_Runoff/Difference/annual/diff_total_m.tif")

'''Precipitation ERA5'''
env.workspace = r"Y:/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Resampled/yearly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
mean = arcpy.sa.Raster(mean) * 1000
mean.save(r"Y:/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Resampled/annual/ERA5_total_y.tif")

env.workspace = r"Y:/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Resampled/monthly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
sum = arcpy.sa.Raster(sum) * 1000
sum.save(r"Y:/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Resampled/annual/ERA5_total_m.tif")

'''Precipitation ERAI'''
env.workspace = r"Y:/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF_Resampled/yearly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
mean = arcpy.sa.Raster(mean) * 1000
mean.save(r"Y:/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF_Resampled/annual/ERAI_total_y.tif")

env.workspace = r"Y:/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF_Resampled/monthly/"
rasters = arcpy.ListRasters()
print (rasters)
#Run Cell Statistics
sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
sum = arcpy.sa.Raster(sum) * 1000
sum.save(r"Y:/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF_Resampled/annual/ERAI_total_m.tif")


#Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)

	########

