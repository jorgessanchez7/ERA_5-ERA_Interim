#!/usr/bin/env python
"""
Get the mean value of the clipped rasters
"""

import os
import gdal
import numpy as np
import pandas as pd
import datetime as dt
import ogr



#ERA-5
ini_date = dt.datetime(1979,1,1,00,00)
end_date = dt.datetime(2020,4,1,00,00)

time_series = np.arange(ini_date, end_date, dt.timedelta(days=1)).astype(dt.datetime)

regions = ['japan-geoglows', 'islands-geoglows', 'middle_east-geoglows', 'central_america-geoglows',
           'central_asia-geoglows', 'australia-geoglows', 'south_asia-geoglows', 'east_asia-geoglows',
           'europe-geoglows', 'north_america-geoglows', 'west_asia-geoglows', 'africa-geoglows',
           'south_america-geoglows']

# Folders de trabajo
FldOut = "/Volumes/files/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Clipped/"

for region in regions:

    print('Starting for the region: ' + region)

    dates = []
    values = []

    for time in time_series:
        YYYY = str(time.year)
        MM = str(time.month)
        DD = str(time.day)

        if int(MM) < 10:
            MM = '0' + str(MM)

        if int(DD) < 10:
            DD = '0' + str(DD)

        print(YYYY,'-',MM,'-',DD)

        # ERA-5
        input_raster = gdal.Open(FldOut + region + "/" + YYYY + "/" + MM + "/" + YYYY + "-" + MM + "-" + DD + ".tif")

        stats = input_raster.GetRasterBand(1).GetStatistics(0, 1)

        mean = stats[2]*1000

        dates.append(time)
        values.append(mean)

    pairs = [list(a) for a in zip(dates, values)]
    values_df = pd.DataFrame(pairs, columns=['Datetime', 'Runoff (mm)'])
    values_df.set_index('Datetime', inplace=True)
    values_df.index = pd.to_datetime(values_df.index)

    values_df.to_csv('/Volumes/files/ECMWF_Runoff/ERA_5/Daily_GeoTIFF_Clipped/{0}.csv'.format(region))

    print('Done for the region: ' + region)