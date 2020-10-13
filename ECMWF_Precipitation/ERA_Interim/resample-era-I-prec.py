#from osgeo import gdal, gdalconst
import gdal
import gdalconst
from pathlib import Path

#Work Folder
folder_Input = "/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF"
folder_Output = "/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF_Resampled"

#listas de fechas
#days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
#		'23','24','25','26','27','28']
#days = ['29']
#days = ['29', '30']
days = ['31']
#months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#months = ['02']
#months = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months = ['01', '03', '05', '07', '08', '10', '12']
#years = ['1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']
years = ['1979']
#years = ['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992',
#		 '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
#		 '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
#years =['2019']

for year in years:
    for month in months:
        for day in days:

            inputfile =  folder_Input + "/" + year + "/" + month + "/" + year + "-" + month + "-" + day + ".tif"
            input = gdal.Open(inputfile, gdalconst.GA_ReadOnly)
            inputProj = input.GetProjection()
            inputTrans = input.GetGeoTransform()

            path = Path('/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}/{0}-{1}-{2}.tif'.format(year, month, day))

            if path.exists():
                referencefile = '/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/{0}/{1}/{0}-{1}-{2}.tif'.format(year, month, day)
            else:
                referencefile = '/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF/1980/01/1980-01-01.tif'
            reference = gdal.Open(referencefile, gdalconst.GA_ReadOnly)
            referenceProj = reference.GetProjection()
            referenceTrans = reference.GetGeoTransform()
            bandreference = reference.GetRasterBand(1)
            x = reference.RasterXSize
            y = reference.RasterYSize

            outputfile = folder_Output + "/" + year + "/" + month + "/" + year + "-" + month + "-" + day + ".tif"
            driver= gdal.GetDriverByName('GTiff')
            output = driver.Create(outputfile,x,y,1,bandreference.DataType)
            output.SetGeoTransform(referenceTrans)
            output.SetProjection(referenceProj)

            gdal.ReprojectImage(input,output,inputProj,referenceProj,gdalconst.GRA_Bilinear)

            FECHA = year + "-" + month + "-" + day
            print(FECHA)

            del output