from django.db import models


class Guides(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    markdown = models.TextField(blank=True, null=True)
    markup = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_image_url = models.CharField(max_length=255, blank=True, null=True)
    article_source_url = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    exerpt = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    reference_domain = models.CharField(max_length=255, blank=True, null=True)
    views_count = models.IntegerField()
    likers_count = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guides'
