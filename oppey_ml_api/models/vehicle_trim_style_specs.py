from django.db import models


class VehicleTrimStyleSpecs(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_trim_style = models.ForeignKey('VehicleTrimStyles', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    inclusion = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_trim_style_specs'
