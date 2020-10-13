#!/usr/bin/env python
"""
Extract Punctual Daily Precipitation from raster".
"""
#from osgeo import gdal, osr, gdal_array
import gdal
import osr
import gdalnumeric as gdal_array
import xarray as xr
import numpy as np
import sys

def GetnetCDFInfobyName(in_filename, var_name):
	"""
	Function to read the original file's projection
	"""

	# Open netCDF file
	src_ds = gdal.Open(in_filename)
	if src_ds is None:
		print ("Open failed")
		sys.exit()

	# If exits more than one var in the NetCDF...
	subdataset = 'NETCDF:"'+ in_filename + '":' + var_name
	src_ds_sd = gdal.Open(subdataset)
	# begin to read info of the named variable (i.e., subdataset)
	NDV = src_ds_sd.GetRasterBand(1).GetNoDataValue()
	xsize = src_ds_sd.RasterXSize
	ysize = src_ds_sd.RasterYSize
	GeoT = src_ds_sd.GetGeoTransform()
	Projection = osr.SpatialReference()
	Projection.ImportFromWkt(src_ds_sd.GetProjectionRef())
	# Close the subdataset and the whole dataset
	src_ds_sd = None
	src_ds = None
	# read data using xarray
	xr_ensemble = xr.open_dataset(in_filename)
	data = xr_ensemble[var_name]
	data = np.ma.masked_array(data, mask=data==NDV,fill_value=NDV)

	return NDV, xsize, ysize, GeoT, Projection, data

def create_geotiff(suffix, Array, NDV, xsize, ysize, GeoT, Projection):
	'''
	Creates new GeoTiff from array
	'''
	DataType = gdal_array.NumericTypeCodeToGDALTypeCode(Array.dtype)

	if type(DataType)!=np.int:
		if DataType.startswith('gdal.GDT_')==False:
			DataType=eval('gdal.GDT_'+DataType)

	NewFileName = suffix + '.tif'
	zsize = Array.shape[0]

	# create a driver
	driver = gdal.GetDriverByName('GTiff')
	# Set nans to the originnal No Data Value
	Array[np.isnan(Array)] = NDV
	# Set up the dataset with zsize bands
	DataSet = driver.Create(NewFileName, xsize, ysize, zsize, DataType)
	DataSet.SetGeoTransform(GeoT)
	DataSet.SetProjection(Projection.ExportToWkt())
	# Write each slice of the array along the zsize
	for i in range(0, zsize):
		DataSet.GetRasterBand(i+1).WriteArray(Array[i])
		DataSet.GetRasterBand(i+1).SetNoDataValue(NDV)

	DataSet.FlushCache()
	return NewFileName

'''
-----------------------------------------------------------------------------------------------------------------------
'''

#Work Folder
'''ERA 5 Precipitation'''
#folder_Input = "/Volumes/files/ECMWF_Precipitation/ERA_5/Daily/"
#folder_Output = "/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/"
'''ERA Interim Precipitation'''
#folder_Input = "/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily/"
#folder_Output = "/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF/"
'''ERA 5 Runoff'''
#folder_Input = "/Volumes/files/ECMWF_Runoff/ERA_5/Daily/"
#folder_Output = "/Volumes/files/ECMWF_Runoff/ERA_5/Daily_GeoTIFF/"
'''ERA Interim Runoff'''
folder_Input = "/Volumes/files/ECMWF_Runoff/ERA_Interim/Daily/"
folder_Output = "/Volumes/files/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF/"

#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
#		'23','24','25','26','27','28']
days = ['29']
#days = ['29', '30']
#days = ['31']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months = ['02']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['01', '03', '05', '07', '08', '10', '12']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']
#years = ['1979']
#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992',
#		 '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
#		 '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
years =['1980']

for year in years:
	for month in months:
		for day in days:

			infile = folder_Input + '{0}-{1}-{2}.nc'.format(year, month, day)
			print(infile)
			var_name = 'tp'
			NDV, xsize, ysize, GeoT, Projection, data = GetnetCDFInfobyName(infile, var_name)
			outfile_name = folder_Output + '{0}-{1}-{2}'.format(year, month, day)
			outfile = create_geotiff(outfile_name, data, NDV, xsize, ysize, GeoT, Projection)
