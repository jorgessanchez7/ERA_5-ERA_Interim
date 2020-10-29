######
#TRANFORMACION DE MAPAS DEL FORMATO NETCDF A RASTERS GEOTIFF
######

# Import system modules  (Importa ArcGis)
import os
import arcpy
from arcpy import env

# Folders de trabajo
FldOn = "Y:\\ECMWF_Precipitation\\"

arcpy.CheckOutExtension("Spatial")


#listas de fechas
listames = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
listaano = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

#Iterar sobre los mapas
for ano in listaano:
	for mes in listames:
		
		#Datos de salida
		FldInPREC_diff = FldOn + "Difference\\{0}\\{1}\\".format(ano,mes)
		FldInPREC_ERA5 = FldOn + "ERA_5/Daily_GeoTIFF/{0}/{1}/".format(ano,mes)
		FldInPREC_ERAI = FldOn + "ERA_Interim/Daily_GeoTIFF_Resampled/{0}/{1}/".format(ano,mes)
		
		
		'''Precipitation'''
		#Define input workspace and create list of rasters
		env.workspace = FldInPREC_diff
		print (FldInPREC_diff)
		rasters = arcpy.ListRasters()
		print (rasters)
		
		#Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
		#mean.save(r"Y:/ECMWF_Precipitation/Difference/{0}/{1}-{2}.tif".format(ano,ano,mes))
		mean.save(r"Y:/ECMWF_Precipitation/Difference/{0}-{1}.tif".format(ano,mes))		
		
		#Define input workspace and create list of rasters
		env.workspace = FldInPREC_ERA5
		rasters = arcpy.ListRasters()
		#print (rasters)
		
		#Run Cell Statistics
		sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
		#sum.save(r"Y:/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}-{2}.tif".format(ano,ano,mes))		
		sum.save(r"Y:/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}-{1}.tif".format(ano,mes))	
        
		#Define input workspace and create list of rasters
		env.workspace = FldInPREC_ERAI
		rasters = arcpy.ListRasters()
		#print (rasters)
		
		#Run Cell Statistics
		sum = arcpy.sa.CellStatistics(rasters, statistics_type = "SUM")
		#sum.save(r"Y:/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/{0}/{1}-{2}.tif".format(ano,ano,mes))		
		sum.save(r"Y:/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/{0}-{1}.tif".format(ano,mes))			
			
		FECHA = ano + "-" + mes
		print (FECHA)
			
			
			#Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)