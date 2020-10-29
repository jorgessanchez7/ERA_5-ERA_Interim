######
#TRANFORMACION DE MAPAS DEL FORMATO NETCDF A RASTERS GEOTIFF
######

# Import system modules  (Importa ArcGis)
import os
import arcpy
from arcpy import env

# Folders de trabajo
FldOn = "Y:/ECMWF_Runoff/"

arcpy.CheckOutExtension("Spatial")


#listas de fechas
listames = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
listaano = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']

#Iterar sobre los mapas
for ano in listaano:
	
	#Datos de salida
	FldInRO_diff = FldOn + "Difference/{0}/".format(ano)
	FldInRO_ERA5 = FldOn + "ERA_5/Daily_GeoTIFF_Resampled/{0}/".format(ano)
	FldInRO_ERAI = FldOn + "ERA_Interim/Daily_GeoTIFF_Resampled/{0}/".format(ano)
	
	'''Runoff'''
	#Define input workspace and create list of rasters
	env.workspace = FldInRO_diff
	rasters = arcpy.ListRasters()
	print (rasters)
	
	#Run Cell Statistics
	mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
	mean.save(r"Y:/ECMWF_Runoff/Difference/yearly/{0}.tif".format(ano))
	
	env.workspace = FldInRO_ERA5
	rasters = arcpy.ListRasters()
	print (rasters)
	
	#Run Cell Statistics
	sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
	sum.save(r"Y:/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Resampled/yearly/{0}.tif".format(ano))
	
	env.workspace = FldInRO_ERAI
	rasters = arcpy.ListRasters()
	print (rasters)
	
	#Run Cell Statistics
	sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
	sum.save(r"Y:/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF_Resampled/yearly/{0}.tif".format(ano))
	
	FECHA = ano
	print (FECHA)
			
			
#Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)
#######

