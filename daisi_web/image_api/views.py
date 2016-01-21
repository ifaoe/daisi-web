from django.shortcuts import HttpResponse
from django.db import connections
from django.contrib.gis.gdal import GDALRaster
# from osgeo import gdal
import os
import tempfile

# Create your views here.

def get_image(request, session, cam, img, utm_x, utm_y, width, height):
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT DISTINCT path FROM projects WHERE project_id=%s", (session,))
    result = cursor.fetchone()
    src_file = os.path.join(result[0],'cam%s' % cam, 'geo', img + '.tif')

    # src_ds = gdal.Open(src_file)
    # driver = gdal.GetDriverByName("GTiff")
    # rstfile = tempfile.NamedTemporaryFile(suffix='.tif')
    # data = driver.CreateCopy(rstfile.name, src_ds, 0, ["COMPRESS=JPEG"])

    rst = GDALRaster(src_file, write=False)
    response = HttpResponse(rst, content_type='image/tiff')
    response['Content-Disposition'] = 'attachment; filename=%s%s%s.tif' % (session, cam, img)
    return response
