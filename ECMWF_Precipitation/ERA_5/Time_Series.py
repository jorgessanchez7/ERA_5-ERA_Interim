######
#CALCULAR LA PRECICIPITACION MEDIA DE LA CUENCA PARA LA SERIE DE TIEMPO
######

# Import system modules  (Importa ArcGis)
import os
import datetime as dt
import numpy as np
import pandas as pd
import arcpy
from arcpy import env
from decimal import *

# Folders de trabajo
FldOn = "Y:\\ECMWF_Precipitation\\ERA_5\\Daily_GeoTIFF_Clipped\\"
FldOut = "Y:\\ECMWF_Precipitation\\ERA_5\\Daily_GeoTIFF_Clipped\\"

# ERA-5
ini_date = dt.datetime(1979, 1, 2, 00, 00)
end_date = dt.datetime(2019, 12, 31, 00, 00)

time_series = np.arange(ini_date, end_date, dt.timedelta(days=1)).astype(dt.datetime)

#lista de cuencas
list_regions = ['Subbasin289', 'africa-geoglows', 'australia-geoglows', 'central_america-geoglows', 'central_asia-geoglows',
                'east_asia-geoglows', 'europe-geoglows', 'islands-geoglows', 'japan-geoglows', 'middle_east-geoglows',
                'north_america-geoglows', 'south_america-geoglows', 'south_asia-geoglows', 'west_asia-geoglows']
 
#Datos de salida
for region in list_regions:
    folder_Output = FldOut + region
    
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
        
        FileOnPREC = folder_Output + "\\" + YYYY + "\\" + MM + "\\" + YYYY + "-" + MM + "-" + DD + ".tif"
        #print(FileOnPREC)
        PrecMeanResult = arcpy.GetRasterProperties_management(FileOnPREC, "MEAN")
        PrecMean = PrecMeanResult.getOutput(0)
        #print(PrecMean)
        #print(type(PrecMean))
        
        dates.append(time)
        values.append((Decimal(PrecMean))*1000)
        #print((Decimal(PrecMean))*1000)
        
        print (region + '-' + YYYY + '-' + MM  + '-' + DD)
    
    pairs = [list(a) for a in zip(dates, values)]
    values_df = pd.DataFrame(pairs, columns=['Datetime', 'Precipitation (mm)'])
    values_df.set_index('Datetime', inplace=True)
    values_df.index = pd.to_datetime(values_df.index)
    values_df.to_csv(FldOut + region + '.csv')
    
    #Finaliza
    
    Fin = '{0}.csv TERMINADO------------'.format(region)
    print (Fin)

print ('Final')

########

