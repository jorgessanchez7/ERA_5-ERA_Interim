######
#TRANFORMACION DE MAPAS DEL FORMATO NETCDF A RASTERS GEOTIFF
######

# Import system modules  (Importa ArcGis)
import os
import arcpy
from arcpy import env

# Folders de trabajo
FldOn = "Y:/ECMWF_Precipitation/"

arcpy.CheckOutExtension("Spatial")


#listas de fechas
listames = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
listaano_1 = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
listaano_2 = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

#Iterar sobre los mapas
for mes in listames:
	
	rasters_PREC_diff = []
	rasters_PREC_ERA5 = []
	rasters_PREC_ERAI = []

	if int(mes) < 9:

		for ano in listaano_1:

			#Datos de salida
			FldInPREC_diff = FldOn + "Difference/{0}/".format(ano)
			FldInPREC_ERA5 = FldOn + "ERA_5/Daily_GeoTIFF/{0}/".format(ano)
			FldInPREC_ERAI = FldOn + "ERA_Interim/Daily_GeoTIFF_Resampled/{0}/".format(ano)

			rasters_PREC_diff.append(FldInPREC_diff + "{0}-{1}.tif".format(ano,mes))
			rasters_PREC_ERA5.append(FldInPREC_ERA5 + "{0}-{1}.tif".format(ano,mes))
			rasters_PREC_ERAI.append(FldInPREC_ERAI + "{0}-{1}.tif".format(ano,mes))

		'''Precipitation'''
		print (rasters_PREC_diff)
		#Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_diff, statistics_type = "MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/Difference/monthly/{0}.tif".format(mes))

		print (rasters_PREC_ERA5)
		#Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_ERA5, statistics_type = "MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/monthly/{0}.tif".format(mes))

		print (rasters_PREC_ERAI)
		#Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_ERAI, statistics_type = "MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/monthly/{0}.tif".format(mes))

		FECHA = mes
		print (FECHA)

	else:

		for ano in listaano_2:
			# Datos de salida
			FldInPREC_diff = FldOn + "Difference/{0}/".format(ano)
			FldInPREC_ERA5 = FldOn + "ERA_5/Daily_GeoTIFF/{0}/".format(ano)
			FldInPREC_ERAI = FldOn + "ERA_Interim/Daily_GeoTIFF_Resampled/{0}/".format(ano)

			rasters_PREC_diff.append(FldInPREC_diff + "{0}-{1}.tif".format(ano, mes))
			rasters_PREC_ERA5.append(FldInPREC_ERA5 + "{0}-{1}.tif".format(ano, mes))
			rasters_PREC_ERAI.append(FldInPREC_ERAI + "{0}-{1}.tif".format(ano, mes))

		'''Precipitation'''
		print(rasters_PREC_diff)
		# Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_diff, statistics_type="MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/Difference/monthly/{0}.tif".format(mes))

		print(rasters_PREC_ERA5)
		# Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_ERA5, statistics_type="MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/monthly/{0}.tif".format(mes))

		print(rasters_PREC_ERAI)
		# Run Cell Statistics
		mean = arcpy.sa.CellStatistics(rasters_PREC_ERAI, statistics_type="MEAN")
		mean.save(r"Y:/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/monthly/{0}.tif".format(mes))

		FECHA = mes
		print(FECHA)

	
#Finaliza
Fin = '------------TRANSFORMACION TERMINADA------------'
print (Fin)