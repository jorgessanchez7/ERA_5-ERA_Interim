#!/usr/bin/env python
"""
Clip Daily Runoff from raster using regions shapefiles".
"""

import gdal
import gdalnumeric
import gdalconst
import ogr
import json
from PIL import Image, ImageDraw
from osgeo import gdal_array

def gdal_clip(raster_input, raster_output, polygon_json, nodata=-32768):
    """
    This function will subset a raster by a vector polygon.
    Adapted from the GDAL/OGR Python Cookbook at
    https://pcjericks.github.io/py-gdalogr-cookbook
    :param raster_input: raster input filepath
    :param raster_output: raster output filepath
    :param polygon_json: polygon as geojson string
    :param nodata: nodata value for output raster file
    :return:
    """

    def image_to_array(i):
        """
        Converts a Python Imaging Library array to a
        gdalnumeric image.
        """
        a = gdalnumeric.numpy.fromstring(i.tobytes(), 'b')
        a.shape = i.im.size[1], i.im.size[0]
        return a

    def world_to_pixel(geoMatrix, x, y):
        """
        Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
        the pixel location of a geospatial coordinate
        """
        ulX = geoMatrix[0]
        ulY = geoMatrix[3]
        xDist = geoMatrix[1]
        pixel = int((x - ulX) / xDist)
        line = int((ulY - y) / xDist)
        return (pixel, line)

    def OpenArray_T(array, prototype_ds=None, xoff=0, yoff=0):
        """
        EDIT: this is basically an overloaded
        version of the gdal_array.OpenArray passing in xoff, yoff explicitly
        so we can pass these params off to CopyDatasetInfo
        """

        #ds = gdal.Open(gdalnumeric.GetArrayFilename(array))
        ds = gdal_array.OpenArray(array)

        if ds is not None and prototype_ds is not None:
            if type(prototype_ds).__name__ == 'str':
                prototype_ds = gdal.Open(prototype_ds)
            if prototype_ds is not None:
                gdalnumeric.CopyDatasetInfo(
                    prototype_ds, ds, xoff=xoff, yoff=yoff)
        return ds

    src_image = get_dataset(raster_input)
    # Load the source data as a gdalnumeric array
    src_array = src_image.ReadAsArray()
    src_dtype = src_array.dtype

    # Also load as a gdal image to get geotransform
    # (world file) info
    geo_trans = src_image.GetGeoTransform()
    nodata_values = []
    for i in range(src_image.RasterCount):
        nodata_value = src_image.GetRasterBand(i+1).GetNoDataValue()
        if not nodata_value:
            nodata_value = nodata
        nodata_values.append(nodata_value)

    # Create an OGR layer from a boundary GeoJSON geometry string
    if type(polygon_json) == dict:
        polygon_json = json.dumps(polygon_json)
    poly = ogr.CreateGeometryFromJson(polygon_json)

    # Convert the layer extent to image pixel coordinates
    min_x, max_x, min_y, max_y = poly.GetEnvelope()
    ul_x, ul_y = world_to_pixel(geo_trans, min_x, max_y)
    lr_x, lr_y = world_to_pixel(geo_trans, max_x, min_y)

    # Calculate the pixel size of the new image
    px_width = int(lr_x - ul_x)
    px_height = int(lr_y - ul_y)

    clip = src_array[ul_y:lr_y, ul_x:lr_x]

    # create pixel offset to pass to new image Projection info
    xoffset = ul_x
    yoffset = ul_y

    # Create a new geomatrix for the image
    geo_trans = list(geo_trans)
    geo_trans[0] = min_x
    geo_trans[3] = max_y

    # Map points to pixels for drawing the
    # boundary on a blank 8-bit,
    # black and white, mask image.
    raster_poly = Image.new("L", (px_width, px_height), 1)
    rasterize = ImageDraw.Draw(raster_poly)
    geometry_count = poly.GetGeometryCount()
    for i in range(0, geometry_count):
        points = []
        pixels = []
        pts = poly.GetGeometryRef(i)
        if pts.GetPointCount() == 0:
            pts = pts.GetGeometryRef(0)
        for p in range(pts.GetPointCount()):
            points.append((pts.GetX(p), pts.GetY(p)))
        for p in points:
            pixels.append(world_to_pixel(geo_trans, p[0], p[1]))
        rasterize.polygon(pixels, 0)
    mask = image_to_array(raster_poly)

    # Clip the image using the mask
    clip = gdalnumeric.numpy.choose(
        mask, (clip, nodata_value)).astype(src_dtype)

    gtiff_driver = gdal.GetDriverByName('GTiff')
    if gtiff_driver is None:
        raise ValueError("Can't find GeoTiff Driver")
    subset_raster = gtiff_driver.CreateCopy(
        raster_output, OpenArray_T(
            clip, prototype_ds=raster_input, xoff=xoffset, yoff=yoffset)
    )
    for i in range(subset_raster.RasterCount):
        band = subset_raster.GetRasterBand(i+1)
        band.SetNoDataValue(nodata_values[i])
    return subset_raster

def get_dataset(object):
    """
    Given an object, try returning a GDAL Dataset
    :param object:
    :return:
    """
    if type(object).__name__ == 'Dataset':
        return object
    else:
        return gdal.Open(object, gdalconst.GA_ReadOnly)


import datetime as dt
import numpy as np
import gdal

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
        input_raster = '/Volumes/files/ECMWF_Runoff/ERA_5/Daily_GeoTIFF/{0}/{1}/{2}-{3}-{4}.tif'.format(YYYY, MM, YYYY, MM, DD)
        output_raster = FldOut + region + "/" + YYYY + "/" + MM + "/" + YYYY + "-" + MM + "-" + DD + ".tif"

        polygon_dir = FldOut + "Regions_SFPT_WGS84/" + region + ".json"
        with open(polygon_dir, 'r') as json_data:
            polygon_file = json.loads(json_data.read())

            gdal_clip(raster_input=input_raster, raster_output=output_raster, polygon_json=polygon_file, nodata=-32768)

    print('Done for the region: ' + region)