# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import models


class AbioticObjects(models.Model):
    object_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abiotic_objects'


class BshTrip(models.Model):
    trip_id = models.IntegerField(blank=True, null=True)
    cruiseno = models.TextField(primary_key=True)
    owpas = models.TextField(blank=True, null=True)
    project = models.TextField(blank=True, null=True)
    cluster = models.TextField(blank=True, null=True)
    lab = models.TextField(blank=True, null=True)
    scientist = models.TextField(blank=True, null=True)
    datatype = models.TextField(blank=True, null=True)
    technique = models.TextField(blank=True, null=True)
    observer = models.TextField(blank=True, null=True)
    plane = models.TextField(blank=True, null=True)
    number_of_planes = models.IntegerField(blank=True, null=True)
    double_platform = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    camera_system = models.TextField(blank=True, null=True)
    resolution = models.FloatField(blank=True, null=True)
    plane_flight_height_planned = models.FloatField(blank=True, null=True)
    strip_width = models.FloatField(blank=True, null=True)
    plane_speed = models.FloatField(blank=True, null=True)
    position_accuracy = models.FloatField(blank=True, null=True)
    method_id = models.IntegerField(blank=True, null=True)
    area_observed = models.FloatField(blank=True, null=True)
    area_analysed = models.FloatField(blank=True, null=True)
    positionsystem = models.TextField(blank=True, null=True)
    posit_precision_code = models.IntegerField(blank=True, null=True)
    refsystem = models.TextField(blank=True, null=True)
    project_key = models.TextField(blank=True, null=True)
    trip_date = models.TextField(blank=True, null=True)
    import_id = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bsh_trip'


class Census(models.Model):
    fcns_id = models.AutoField(primary_key=True)
    rcns_id = models.IntegerField(blank=True, null=True)
    usr = models.TextField(blank=True, null=True)
    tp = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    beh = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    gen = models.TextField(blank=True, null=True)
    dir = models.IntegerField(blank=True, null=True)
    rem = models.TextField(blank=True, null=True)
    censor = models.IntegerField(blank=True, null=True)
    imgqual = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    stuk4_ass = models.TextField(blank=True, null=True)  # This field type is a guess.
    stuk4_beh = models.TextField(blank=True, null=True)  # This field type is a guess.
    group_objects = models.TextField(blank=True, null=True)  # This field type is a guess.
    family_group = models.TextField(blank=True, null=True)  # This field type is a guess.
    age_year = models.IntegerField(blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    id_code = models.TextField(blank=True, null=True)
    plumage = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(blank=True, null=True)
    time_modify = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census'


class ImageProperties(models.Model):
    _DATABASE = 'daisi'
    img_id = models.BigIntegerField(primary_key=True)
    sync_id = models.IntegerField()
    session = models.TextField()
    cam = models.TextField()
    img = models.TextField()
    glare_key = models.FloatField(blank=True, null=True)
    cut_env = models.TextField(blank=True, null=True)  # This field type is a guess.
    seastate = models.IntegerField(blank=True, null=True)
    turbidity = models.IntegerField(blank=True, null=True)
    ice = models.FloatField(blank=True, null=True)
    clarity = models.TextField(blank=True, null=True)
    analysed = models.NullBooleanField()
    trc = models.IntegerField(blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
#    project_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    project_list = ArrayField(models.TextField(blank=True, null=True))
    remarks = models.TextField(blank=True, null=True)
    glare_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_properties'


class Projects(models.Model):
    _DATABASE = 'daisi'
    project_id = models.TextField(primary_key=True)
    flight_id = models.TextField(blank=True, null=True)
    utm_sector = models.IntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    image_filter = models.TextField(blank=True, null=True)
    session_type = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class RawCensus(models.Model):
    rcns_id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=64, blank=True, null=True)
    epsg = models.IntegerField(blank=True, null=True)
    cam = models.CharField(max_length=5, blank=True, null=True)
    img = models.CharField(max_length=64, blank=True, null=True)
    tp = models.TextField(blank=True, null=True)
    px = models.IntegerField(blank=True, null=True)
    py = models.IntegerField(blank=True, null=True)
    ux = models.FloatField(blank=True, null=True)
    uy = models.FloatField(blank=True, null=True)
    lx = models.FloatField(blank=True, null=True)
    ly = models.FloatField(blank=True, null=True)
    usr = models.CharField(max_length=32, blank=True, null=True)
    tm_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_census'


class RawImages(models.Model):
    _DATABASE = 'daisi'
    rimg_id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=64, blank=True, null=True)
    epsg = models.IntegerField(blank=True, null=True)
    cam = models.CharField(max_length=5, blank=True, null=True)
    img = models.CharField(max_length=64, blank=True, null=True)
    usr = models.CharField(max_length=32, blank=True, null=True)
    rdy = models.IntegerField(blank=True, null=True)
    tm_when = models.TextField(blank=True, null=True)
    tm_seen = models.TextField(blank=True, null=True)
    tm_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_images'


class RawTiles(models.Model):
    rtls_id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=64, blank=True, null=True)
    epsg = models.IntegerField(blank=True, null=True)
    cam = models.CharField(max_length=5, blank=True, null=True)
    img = models.CharField(max_length=64, blank=True, null=True)
    usr = models.CharField(max_length=32, blank=True, null=True)
    ux = models.TextField(blank=True, null=True)
    uy = models.TextField(blank=True, null=True)
    w = models.TextField(blank=True, null=True)
    h = models.TextField(blank=True, null=True)
    tm_when = models.TextField(blank=True, null=True)
    tm_seen = models.TextField(blank=True, null=True)
    tm_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_tiles'

        
class Stuk4Codes(models.Model):
    code_id = models.AutoField(primary_key=True)
    code = models.TextField()
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type = models.TextField()
    category_en = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    remarks_en = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stuk4_codes'


class SyncUtm32(models.Model):
    _DATABASE = 'daisi'
    sync_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    session = models.CharField(max_length=64, blank=True, null=True)
    prj_id = models.IntegerField(blank=True, null=True)
    gps_id = models.IntegerField(blank=True, null=True)
    gps_trc = models.IntegerField(blank=True, null=True)
    gps_img = models.IntegerField(blank=True, null=True)
    gps_dt = models.DateField(blank=True, null=True)
    gps_tm = models.TimeField(blank=True, null=True)
    gps_ts = models.IntegerField(blank=True, null=True)
    cam1_id = models.CharField(max_length=64, blank=True, null=True)
    cam1_dt = models.DateField(blank=True, null=True)
    cam1_tm = models.TimeField(blank=True, null=True)
    cam1_ts = models.IntegerField(blank=True, null=True)
    cam1_cts = models.IntegerField(blank=True, null=True)
    cam1_dts = models.IntegerField(blank=True, null=True)
    cam1_oclk = models.IntegerField(blank=True, null=True)
    cam1_tclk = models.IntegerField(blank=True, null=True)
    cam1_cfg = models.CharField(max_length=4, blank=True, null=True)
    cam2_id = models.CharField(max_length=64, blank=True, null=True)
    cam2_dt = models.DateField(blank=True, null=True)
    cam2_tm = models.TimeField(blank=True, null=True)
    cam2_ts = models.IntegerField(blank=True, null=True)
    cam2_cts = models.IntegerField(blank=True, null=True)
    cam2_dts = models.IntegerField(blank=True, null=True)
    cam2_oclk = models.IntegerField(blank=True, null=True)
    cam2_tclk = models.IntegerField(blank=True, null=True)
    cam2_cfg = models.CharField(max_length=4, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    sog = models.FloatField(blank=True, null=True)
    cog = models.FloatField(blank=True, null=True)
    roll_plane = models.FloatField(blank=True, null=True)
    roll_stabi = models.FloatField(blank=True, null=True)
    pitch_plane = models.FloatField(blank=True, null=True)
    pitch_stabi = models.FloatField(blank=True, null=True)
    head_plane = models.FloatField(blank=True, null=True)
    head_stabi = models.FloatField(blank=True, null=True)
    pp_wx_sb = models.TextField(blank=True, null=True)
    pp_wy_sb = models.TextField(blank=True, null=True)
    pp_wx_bb = models.TextField(blank=True, null=True)
    pp_wy_bb = models.TextField(blank=True, null=True)
    pp_ix_sb = models.TextField(blank=True, null=True)
    pp_iy_sb = models.TextField(blank=True, null=True)
    pp_ix_bb = models.TextField(blank=True, null=True)
    pp_iy_bb = models.TextField(blank=True, null=True)
    geo_nw_bb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_no_bb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_sw_bb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_so_bb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_rc_bb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_nw_sb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_no_sb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_sw_sb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_so_sb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_rc_sb = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_ct = models.TextField(blank=True, null=True)  # This field type is a guess.
    geo_dr = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sync_utm32'


class Taxa(models.Model):
    euring_id = models.TextField(primary_key=True)
    name_lat = models.TextField(blank=True, null=True)
    name_de = models.TextField(blank=True, null=True)
    name_en = models.TextField(blank=True, null=True)
    type = models.TextField()
    seaflag = models.BooleanField()
    custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'taxa'




