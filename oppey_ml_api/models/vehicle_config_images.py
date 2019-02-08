from django.db import models


class VehicleConfigImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_config_id = models.BigIntegerField(blank=True, null=True)
    image_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicle_config_images'
