import os
import glob


def create_tif(path_data, results):
    name = path_data.split('/')[-1].split('.')[0]
    save = f'{results}/{name}.tif'
    os.system(f'gdalwarp -s_srs "+proj=longlat +ellps=WGS84" -wo SOURCE_EXTRA=1000 -t_srs WGS84 -of GTiff  '
              f'--config CENTER_LONG 0  {path_data} {save}')
    pass


def main():
    '''ERA 5 Precipitation'''
    #data = '/Volumes/files/ECMWF_Precipitation/ERA_5/Daily'
    #results = '/Volumes/files/ECMWF_Precipitation/ERA_5/Daily_GeoTIFF'
    '''ERA Interim Precipitation'''
    #data = '/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily'
    #results = '/Volumes/files/ECMWF_Precipitation/ERA_Interim/Daily_GeoTIFF'
    '''ERA 5 Runoff'''
    #data = '/Volumes/files/ECMWF_Runoff/ERA_5/Daily'
    #results = '/Volumes/files/ECMWF_Runoff/ERA_5/Daily_GeoTIFF'
    '''ERA Interim Runoff'''
    data = '/Volumes/files/ECMWF_Runoff/ERA_Interim/Daily'
    results = '/Volumes/files/ECMWF_Runoff/ERA_Interim/Daily_GeoTIFF'
    files = glob.glob(f'{data}/*.nc')
    for file in files:
        print(file)
        create_tif(file, results)


if __name__ == '__main__':
    main()
