#!/usr/bin/env python
"""
Save as get-tp.py, then run "python get-tp.py".

Input file : None
Output file: tp_20180101.nc
"""

from ecmwfapi import ECMWFDataServer
import os

os.chdir('/Volumes/files/ECMWF_Precipitation/ERA_Interim/Hourly')
#os.chdir('Y:\\ECMWF_Precipitation\\ERA_Interim\\Hourly')

server = ECMWFDataServer()

#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992',
#		 '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
#		 '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

years = ['2019']

for year in years:

	if year == '2019':

		server.retrieve({
			"class": "ei",
			"dataset": "interim",
			"date": "{0}-01-01/to/{0}-08-31".format(year),
			"expver": "1",
			"grid": "0.75/0.75",
			"levtype": "sfc",
			"param": "228.128",
			"step": "12",
			"stream": "oper",
			"time": "00:00:00/12:00:00",
			#'time': "00/06/12/18",
			"type": "fc",
			#"type": "an",
			"format": "netcdf",
			"target": "{}.nc".format(year),
		})

	else:
		next_year = str(int(year) + 1)

		server.retrieve({
			"class": "ei",
			"dataset": "interim",
			"date": "{0}-01-01/to/{1}-01-01".format(year, next_year),
			"expver": "1",
			"grid": "0.75/0.75",
			"levtype": "sfc",
			"param": "228.128",
			"step": "12",
			"stream": "oper",
			"time": "00:00:00/12:00:00",
			#'time': "00/06/12/18",
			"type": "fc",
			#"type": "an",
			"format": "netcdf",
			"target": "{}.nc".format(year),
		})