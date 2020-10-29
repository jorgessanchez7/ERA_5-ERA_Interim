######
#CONVERT MAPS FROM NETCDF TO GEOTIFF RASTERS
######

# Import system modules  (Import ArcGis)
import os
import arcpy
from arcpy import env

#Work Folder
folder_input = "Y:\\ECMWF_Precipitation\\Difference"
folder_output = "Y:\\ECMWF_Precipitation\\Clipped_Difference"
FileSHP = "Y:\\ECMWF_Precipitation\\Boundary.shp"

#listas de fechas
#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
#            '22','23','24','25','26','27','28']
#days = ['29']
#days = ['29', '30']
days = ['31']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['02']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months = ['01', '03', '05', '07', '08', '10', '12']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012']
#years = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
#		 '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
#		 '2008', '2009', '2010', '2011', '2012', '2013', '2014']
years = ['2007']

for year in years:
	for month in months:
		for day in days:

			fileInput = folder_input + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif"
			fileOutput = folder_output + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif"

			#Recortar GeoTiFF
			arcpy.Clip_management(fileInput, "#", fileOutput, FileSHP, "1", "ClippingGeometry")

			FECHA = year + "-" + month + "-" + day
			print (FECHA)

# Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)
