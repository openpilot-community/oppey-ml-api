from django.db import models


class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    provider_name = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    html = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uploaded_at = models.DateTimeField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    views_count = models.IntegerField()
    likers_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos'
