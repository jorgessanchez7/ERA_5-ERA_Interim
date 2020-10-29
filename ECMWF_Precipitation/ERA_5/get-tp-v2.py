#!/usr/bin/env python
"""
Save as get-tp.py, then run "python get-tp.py".

Input file : None
Output file: 2017-01.nc
"""


import cdsapi
import os

print(os.getcwd())

os.chdir('/Volumes/files/ECMWF_Precipitation/ERA_5/Hourly')
#os.chdir('Y:\ECMWF_Precipitation\ERA_5\Hourly')

c = cdsapi.Client()

datos = c.retrieve(
	'reanalysis-era5-single-levels',
	{"variable": "total_precipitation",
	 "product_type": "reanalysis",
	 "date": "2019-01-01/2019-12-31",
	 "time": ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
			  '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
			  '22:00', '23:00'],
	 "format": "netcdf"
	 })

datos.download('2019.nc')