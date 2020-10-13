#!/usr/bin/env python
"""
Extract Punctual Daily Precipitation from raster".
"""
import numpy as np
import gdal


def get_value_from_raster(raster_filename, x, y):
	"""
	Get values from a raster file based on given points (x, y)
	:param raster_filename:
	:param y:
	:param x:
	:return:
	"""

	points = np.vstack((x, y)).T
	raster = gdal.Open(raster_filename)
	trans_data = raster.GetGeoTransform()
	band = raster.GetRasterBand(1)
	no_data_value = band.GetNoDataValue()
	values = []

	for point in points:
		mx = point[0]
		my = point[1]
		px = int((mx - trans_data[0]) / trans_data[1])
		py = int((my - trans_data[3]) / trans_data[5])

		try:
			raster_value = band.ReadAsArray(px, py, 1, 1)[0][0]

		except TypeError as e:
			print("Point not found ({}, {}). {}".format(mx, my, e))
			raster_value = no_data_value

		if raster_value == no_data_value:
			raster_value = float('nan')

		values.append(raster_value)

	return values


import datetime as dt
import pandas as pd

# ERA-5
ini_date = dt.datetime(1979, 1, 2, 00, 00)
end_date = dt.datetime(2019, 12, 31, 00, 00)

'''
#ERA-Interim
ini_date = dt.datetime(1979,1,2,00,00)
end_date = dt.datetime(2019,9,1,00,00)
'''

time_series = np.arange(ini_date, end_date, dt.timedelta(days=1)).astype(dt.datetime)

regions = ['japan-geoglows', 'islands-geoglows', 'middle_east-geoglows', 'central_america-geoglows',
           'central_asia-geoglows', 'australia-geoglows', 'south_asia-geoglows', 'east_asia-geoglows',
           'europe-geoglows', 'north_america-geoglows', 'west_asia-geoglows', 'africa-geoglows',
           'south_america-geoglows']

#regions = ['japan-geoglows', 'islands-geoglows', 'middle_east-geoglows', 'central_america-geoglows',
#           'central_asia-geoglows', 'australia-geoglows', 'south_asia-geoglows', 'east_asia-geoglows',
#           'europe-geoglows', 'north_america-geoglows', 'west_asia-geoglows', 'africa-geoglows',
#           'south_america-geoglows']

for region in regions:
	'''
	#Windows
	df = pd.read_csv('Y:\\ECMWF_Precipitation\\Shapes\\{0}.csv'.format(region))
	'''
    
	# Mac
	#df = pd.read_csv('/Volumes/files/ECMWF_Precipitation/Shapes/{0}.csv'.format(region))
	df = pd.read_csv('/Users/ElkiGio/Desktop/ERA_5-ERA_Interim/{0}.csv'.format(region))
    
	'''    
    # Linuex
	df = pd.read_csv('/home/water/mount_to_container/NASdrive/ECMWF_Precipitation/Shapes/{0}.csv'.format(region))
	'''
    
	POINT_Xs = df['POINT_X'].tolist()
	POINT_Ys = df['POINT_Y'].tolist()
	POINTs = df['POINT'].tolist()

	for point_x, point_y, point in zip(POINT_Xs, POINT_Ys, POINTs):
		print(point)

		dates = []
		values = []

		for time in time_series:
			YYYY = str(time.year)
			MM = str(time.month)
			DD = time.day

			if int(MM) < 10:
				MM = '0' + str(MM)

			if int(DD) < 10:
				DD = '0' + str(DD)

			# ERA-5
			#raster_filename = 'Y:\\ECMWF_Precipitation\\ERA_5\\Daily_GeoTIFF\\{0}\\{1}\\{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			#raster_filename = '/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			raster_filename = '/Users/ElkiGio/Desktop/ERA_5-ERA_Interim/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			#raster_filename = '/home/water/mount_to_container/NASdrive/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)

			'''
			# ERA-Interim
			#raster_filename = 'Y:\\ECMWF_Precipitation\\ERA_Interim\\Daily_GeoTIFF_Resampled\\{0}\\{1}\\{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			#raster_filename = '/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			raster_filename = '/home/water/mount_to_container/NASdrive/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
			'''

			value = get_value_from_raster(raster_filename, point_x, point_y)

			dates.append(time)
			values.append(value[0]*1000)

		pairs = [list(a) for a in zip(dates, values)]
		values_df = pd.DataFrame(pairs, columns=['Datetime', 'Precipitation (mm)'])
		values_df.set_index('Datetime', inplace=True)
		values_df.index = pd.to_datetime(values_df.index)

		# ERA 5
		#values_df.to_csv('Y:\\ECMWF_Precipitation\\Time_Series\\ERA_5\\{0}\\{1}.csv'.format(region, point))
		values_df.to_csv('/Volumes/files/ECMWF_Precipitation/Time_Series/ERA_5/{0}/{1}.csv'.format(region, point))
		#values_df.to_csv('/Users/ElkiGio/Desktop/ERA_5-ERA_Interim/ECMWF_Precipitation/ERA_5/{0}/{1}.csv'.format(region, point))
		#values_df.to_csv('/home/water/mount_to_container/NASdrive/ECMWF_Precipitation/Time_Series/ERA_5/{0}/{1}.csv'.format(region, point))

		'''
		#ERA Interim
		#values_df.to_csv('Y:\\ECMWF_Precipitation\\Time_Series\\ERA_Interim\\{0}\\{1}.csv'.format(region, point))
		values_df.to_csv('/Volumes/files/ECMWF_Precipitation/Time_Series/ERA_Interim/{0}/{1}.csv'.format(region, point))
		values_df.to_csv('/home/water/mount_to_container/NASdrive/ECMWF_Precipitation/Time_Series/ERA_Interim/{0}/{1}.csv'.format(region, point))
		'''

	print('Done for the region: ' + region)