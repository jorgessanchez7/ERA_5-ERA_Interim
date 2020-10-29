######
#CONVERT MAPS FROM NETCDF TO GEOTIFF RASTERS
######

# Import system modules  (Import ArcGis)
import os
import arcpy
from arcpy import env

#Work Folder
folder_Input = "Y:\\ECMWF_Runoff\\ERA_5\\ERA-5_Daily_RO"
folder_Output = "Y:\\ECMWF_Runoff\\ERA_5\\Daily_GeoTIFF"

#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
#		'23','24','25','26','27','28']
#days = ['29']
#days = ['29', '30']
#days = ['31']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['02']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '05', '07', '08', '10', '12']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']
#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992',
#		 '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
##		 '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
days = ['30']
months = ['11']
years = ['2014']

for year in years:
	for month in months:
		for day in days:

			# NetCDF Raster layer
			fileInput = folder_Input + "\\" + year + month + day + ".nc"
			fileOutput =  year + "-" + month + "-" + day
			tifOutput = folder_Output + "\\" + year + "\\" + month + "\\" +  year + "-" + month + "-" + day + ".tif"
			arcpy.MakeNetCDFRasterLayer_md(fileInput, "RO", "lon", "lat", fileOutput, "time", "#", "BY_VALUE")
			# Export to GeoTiFF
			arcpy.CopyRaster_management(fileOutput, tifOutput, "#", "#", "-9.999900e+003", "NONE", "NONE", "#", "NONE", "NONE")
			# Define Projection
			# arcpy.DefineProjection_management(tifOutput, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
			# borrar map aux
			arcpy.Delete_management(year + "-" + month + "-" + day)
			# cerrar raster
			# arcpy.Delete_management(tifOutput)

			FECHA = year + "-" + month + "-" + day
			print (FECHA)

# Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)
