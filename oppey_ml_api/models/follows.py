from django.db import models


class Follows(models.Model):
    follower_type = models.CharField(max_length=255, blank=True, null=True)
    follower_id = models.IntegerField(blank=True, null=True)
    followable_type = models.CharField(max_length=255, blank=True, null=True)
    followable_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follows'
