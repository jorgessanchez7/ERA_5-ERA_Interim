######
#CONVERT MAPS FROM NETCDF TO GEOTIFF RASTERS
######

# Import system modules  (Import ArcGis)
import os
import arcpy
from arcpy import env
from arcpy.sa import *

#Work Folder
folder_ERA5 = "Y:\\ECMWF_Precipitation\\ERA_5\\Daily_GeoTIFF"
folder_ERAI = "Y:\\ECMWF_Precipitation\\ERA_Interim\\Daily_GeoTIFF_Resampled"
folder_output = "Y:\\ECMWF_Precipitation\\Difference"

env.workspace = "Y:/ECMWF_Precipitation"

#listas de fechas
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
		'23','24','25','26','27','28']
#days = ['02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23',
#		'24','25','26','27','28']
#days = ['29']
#days = ['29', '30']
#days = ['31']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '02', '03', '04', '05', '06', '07', '08']
#months = ['01']
#months = ['02']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '04', '05', '06', '07', '08']
#months = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '05', '07', '08', '10', '12']
#months = ['01', '03', '05', '07', '08']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']
#years = ['1979']
years = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
		 '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
		 '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
#years = ['2019']

for year in years:
	for month in months:
		for day in days:

			FileSnap = 'Y:\\ECMWF_Precipitation\\ERA_5\\Daily_GeoTIFF\\{0}\\{1}\\{0}-{1}-{2}.tif'.format(year, month, day)

			minuendo = '{0}\\{1}\\{2}\\{1}-{2}-{3}.tif'.format(folder_ERAI, year, month, day)

			sustraendo = '{0}\\{1}\\{2}\\{1}-{2}-{3}.tif'.format(folder_ERA5, year, month, day)

			# Adjust the grid cell to ERA5
			arcpy.env.cellSize = FileSnap
			arcpy.env.extent = FileSnap

			# Difference Calculator
			diferencia = Raster(minuendo) - Raster(sustraendo)
			#diferencia.save(folder_output + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif")
			diferencia.save(folder_output + "\\" + year + "-" + month + "-" + day + ".tif")
            
			FECHA = year + "-" + month + "-" + day
			print (FECHA)

# Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)
