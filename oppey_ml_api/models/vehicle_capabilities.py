from django.db import models


class VehicleCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    vehicle_config_count = models.IntegerField(blank=True, null=True)
    grouping = models.CharField(max_length=255, blank=True, null=True)
    value_type = models.CharField(max_length=255, blank=True, null=True)
    default_string = models.CharField(max_length=255, blank=True, null=True)
    default_timeout = models.CharField(max_length=255, blank=True, null=True)
    default_kph = models.CharField(max_length=255, blank=True, null=True)
    source_image_url = models.CharField(max_length=255, blank=True, null=True)
    default_state = models.IntegerField(blank=True, null=True)
    spec_lookups = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_capabilities'
