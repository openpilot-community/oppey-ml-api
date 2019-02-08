from django.db import models


class CommontatorThreads(models.Model):
    commontable_type = models.CharField(max_length=255, blank=True, null=True)
    commontable_id = models.IntegerField(blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    closer_type = models.CharField(max_length=255, blank=True, null=True)
    closer_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commontator_threads'
        unique_together = (('commontable_id', 'commontable_type'),)
