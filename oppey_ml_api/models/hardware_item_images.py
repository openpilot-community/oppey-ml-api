from django.db import models


class HardwareItemImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    hardware_item_id = models.BigIntegerField(blank=True, null=True)
    image_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hardware_item_images'
