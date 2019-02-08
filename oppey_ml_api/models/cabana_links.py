from django.db import models


class CabanaLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    route_id = models.CharField(max_length=255, blank=True, null=True)
    route_segment = models.CharField(max_length=255, blank=True, null=True)
    route_segment_at = models.DateTimeField(blank=True, null=True)
    segment_url = models.CharField(max_length=255, blank=True, null=True)
    source_cabana_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cabana_links'
