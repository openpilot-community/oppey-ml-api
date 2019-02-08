from django.db import models


class RailsAdminSettings(models.Model):
    enabled = models.NullBooleanField()
    kind = models.CharField(max_length=255)
    ns = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255)
    raw = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rails_admin_settings'
        unique_together = (('ns', 'key'),)
