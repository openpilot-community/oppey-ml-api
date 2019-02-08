from django.db import models


class VehicleConfigGuides(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    guide = models.ForeignKey('Guides', models.DO_NOTHING, blank=True, null=True)
    vehicle_config_type = models.ForeignKey('VehicleConfigTypes', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicle_config_guides'
