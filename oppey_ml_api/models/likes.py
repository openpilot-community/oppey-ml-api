from django.db import models


class Likes(models.Model):
    liker_type = models.CharField(max_length=255, blank=True, null=True)
    liker_id = models.IntegerField(blank=True, null=True)
    likeable_type = models.CharField(max_length=255, blank=True, null=True)
    likeable_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'
