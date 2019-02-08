from django.db import models


class VehicleTrims(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.ForeignKey('VehicleModels', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sort_order = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    user_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_trims'
