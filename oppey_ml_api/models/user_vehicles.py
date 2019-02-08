from django.db import models


class UserVehicles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    vehicle_trim = models.ForeignKey('VehicleTrims', models.DO_NOTHING, blank=True, null=True)
    vehicle_trim_style = models.ForeignKey('VehicleTrimStyles', models.DO_NOTHING, blank=True, null=True)
    source_image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_vehicles'
