from django.db import models


class VehicleLookups(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    vehicle_make = models.ForeignKey('VehicleMakes', models.DO_NOTHING)
    vehicle_model = models.ForeignKey('VehicleModels', models.DO_NOTHING)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    lookup_count = models.IntegerField()
    slug = models.CharField(max_length=255)
    refreshing = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicle_lookups'
