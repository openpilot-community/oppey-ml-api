from django.db import models


class HardwareTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description_markup = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware_types'
