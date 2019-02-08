from django.db import models


class VehicleTrimStyles(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_trim = models.ForeignKey('VehicleTrims', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    inventory_prices = models.CharField(max_length=255, blank=True, null=True)
    mpg = models.CharField(max_length=255, blank=True, null=True)
    engine = models.CharField(max_length=255, blank=True, null=True)
    trans = models.CharField(max_length=255, blank=True, null=True)
    drive = models.CharField(max_length=255, blank=True, null=True)
    colors = models.CharField(max_length=255, blank=True, null=True)
    seats = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_trim_styles'
