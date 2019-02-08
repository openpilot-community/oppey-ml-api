from django.db import models


class VehicleOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    alternate_name = models.CharField(max_length=255, blank=True, null=True)
    what_it_does = models.TextField(blank=True, null=True)
    what_it_doesnt_do = models.TextField(blank=True, null=True)
    reference_url = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_options'
