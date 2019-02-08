from django.db import models


class VehicleModelOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_year = models.IntegerField(blank=True, null=True)
    vehicle_make = models.ForeignKey('VehicleMakes', models.DO_NOTHING, blank=True, null=True)
    vehicle_model = models.ForeignKey('VehicleModels', models.DO_NOTHING, blank=True, null=True)
    vehicle_option = models.ForeignKey('VehicleOptions', models.DO_NOTHING, blank=True, null=True)
    vehicle_option_availability = models.ForeignKey('VehicleOptionAvailabilities', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicle_model_options'
