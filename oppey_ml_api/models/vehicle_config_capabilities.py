from django.db import models


class VehicleConfigCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    vehicle_capability = models.ForeignKey('VehicleCapabilities', models.DO_NOTHING, blank=True, null=True)
    kph = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    confirmed = models.NullBooleanField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    vehicle_config_type_id = models.BigIntegerField(blank=True, null=True)
    confirmed_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    string_value = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_config_capabilities'
