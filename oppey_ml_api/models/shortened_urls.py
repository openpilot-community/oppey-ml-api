from django.db import models


class ShortenedUrls(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    owner_type = models.CharField(max_length=20, blank=True, null=True)
    url = models.TextField()
    unique_key = models.CharField(unique=True, max_length=10)
    category = models.CharField(max_length=255, blank=True, null=True)
    use_count = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shortened_urls'
