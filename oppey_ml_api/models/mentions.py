from django.db import models


class Mentions(models.Model):
    mentioner_type = models.CharField(max_length=255, blank=True, null=True)
    mentioner_id = models.IntegerField(blank=True, null=True)
    mentionable_type = models.CharField(max_length=255, blank=True, null=True)
    mentionable_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mentions'
