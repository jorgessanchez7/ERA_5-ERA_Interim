######
#RECORTAR LOS DIFERENTES RASTERS METEOROLOGICOS A LAS SUBCUENCAS DE INTERES
######

# Import system modules  (Importa ArcGis)
import os
import arcpy
from arcpy import env

# Folders de trabajo
folder_Input = "Y:\\ECMWF_Precipitation\\ERA_Interim\\Daily_GeoTIFF\\"
#folder_Input = "Y:\\ECMWF_Precipitation\\ERA_Interim\\Daily_GeoTIFF_Resampled\\"
FldOut = "Y:\\ECMWF_Precipitation\\ERA_Interim\\Daily_GeoTIFF_Clipped\\"

#lista de cuencas
#list_regions = ['africa-geoglows', 'australia-geoglows', 'central_america-geoglows', 'central_asia-geoglows',
#				'east_asia-geoglows', 'europe-geoglows', 'islands-geoglows', 'japan-geoglows', 'middle_east-geoglows',
#				'north_america-geoglows', 'south_america-geoglows', 'south_asia-geoglows', 'west_asia-geoglows', 'Subbasin289']
list_regions = ['islands-geoglows', 'japan-geoglows', 'middle_east-geoglows', 'north_america-geoglows', 'south_america-geoglows', 'south_asia-geoglows', 'west_asia-geoglows', 'Subbasin289']


#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '02', '03', '04', '05', '06', '07', '08']
#years = ['1979']
#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
#		 '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
#		 '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
#years = ['2019']
years = ['2001']
months = ['10']

#30's dias
#days = ['29', '30']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '04', '05', '06', '07', '08']

#31's dias
#days = ['31']
#months = ['01', '03', '05', '07', '08', '10', '12']
#months = ['01', '03', '05', '07', '08']

#Bisiestos
#days = ['29']
#months = ['02']
#years = ['1980','1984','1988','1992', '1996', '2000', '2004', '2008', '2012', '2016']

#Datos de salida
for region  in list_regions:
	folder_Output = FldOut + region
	FileSHP = FldOut + "\\Regions_SFPT_WGS84\\" + region + ".shp"
	
	#Iterar sobre los mapas
	for year in years:
		for month in months:
			for day in days:
				#Brillo Solar
				#Entrada y Salida
				fileInput = folder_Input + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif"
				fileOutput = folder_Output + "\\" + year + "\\" + month + "\\" + year + "-" + month + "-" + day + ".tif"
				#Recortar GeoTiFF
				arcpy.Clip_management(fileInput, "#", fileOutput, FileSHP, "1", "ClippingGeometry")
				
				FECHA = region + "_" + year + "-" + month + "-" + day
				print (FECHA)
				
				#Finaliza
				
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)

	########