######
#RESAMPLE TO GEOTIFF RASTERS
######

# Import system modules  (Import ArcGis)
import os
import arcpy
#from arcpy import env
#from arcpy.sa import *

#Work Folder
folder_Input = "Y:\\ECMWF_Runoff\\ERA_5\Daily_GeoTIFF"
folder_Output = "Y:\\ECMWF_Runoff\\ERA_5\\Daily_GeoTIFF_Filled"

#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
#		'23','24','25','26','27','28']
#days = ['29']
#days = ['29', '30']
#days = ['31']
days = ['30']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['02']
months = ['11']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '05', '07', '08', '10', '12']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']
#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
#		 '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
#		 '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
years = ['2014']

for year in years:
	for month in months:
		for day in days:

			try:
				FileSnap = 'Y:\\ECMWF_Runoff\\ERA_5\\Daily_GeoTIFF\\{0}\\{1}\\{0}-{1}-{2}.tif'.format(year, month, day)
			except:
				FileSnap = 'Y:\\ECMWF_Runoff\\ERA_5\\Daily_GeoTIFF\\{0}\\{1}\\1980-01-01.tif'.format(year, month, day)

			# NetCDF Raster layer
			fileInput = folder_Input + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif"
			fileOutput = folder_Output + "\\" + year + "\\" + month + "\\" +  year + "-" + month + "-" + day + ".tif"
			# Change XY Resolution to GeoTiFF
			# Adjust the grid cell to ERA5
			#arcpy.env.cellSize = FileSnap
			#arcpy.env.extent = FileSnap
			#arcpy.env.extent = arcpy.Extent(-0.175781, -90.125, 360.074219, 90.125)
			arcpy.env.extent = arcpy.Extent(-0.140625, -89.924214, 360.140625, 89.924214)            
			#arcpy.env.snapRaster = FileSnap
			filled_raster = arcpy.sa.Con(arcpy.sa.IsNull(arcpy.sa.Raster(fileInput)), arcpy.sa.FocalStatistics(arcpy.sa.Raster(fileInput), arcpy.sa.NbrRectangle(3, 3), 'MEAN'), arcpy.sa.Raster(fileInput))
			filled_raster.save(folder_Output + "\\" + year + "\\" + month + "\\" +  year + "-" + month + "-" + day + ".tif")
			#arcpy.Resample_management (fileInput, fileOutput, "0.25 0.25", "BILINEAR")

			FECHA = year + "-" + month + "-" + day
			print (FECHA)

# Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)
