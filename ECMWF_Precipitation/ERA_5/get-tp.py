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

#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992',
#		 '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
#		 '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
years = ['2007']

for year in years:

	if year == '2019':
		next_year = '2020'

		datos = c.retrieve(
			'reanalysis-era5-single-levels',
			{"variable": "total_precipitation",
			 "product_type": "reanalysis",
			 "date": "{0}-01-01/{1}-01-01".format(year, next_year),
			 "time": ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
					  '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00',
					  '20:00', '21:00', '22:00', '23:00'],
			 "format": "netcdf"
			 })

		datos.download('{0}.nc'.format(year))

	else:
		next_year = str(int(year) + 1)

		datos = c.retrieve(
			'reanalysis-era5-single-levels',
			{ "variable": "total_precipitation",
			  "product_type": "reanalysis",
			  "date": "{0}-01-01/{1}-01-01".format(year, next_year),
			  "time": [ '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
						'10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00',
						'20:00', '21:00', '22:00', '23:00'],
			  "format": "netcdf"
			  })

		datos.download('{0}.nc'.format(year))