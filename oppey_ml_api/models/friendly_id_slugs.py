from django.db import models


class FriendlyIdSlugs(models.Model):
    slug = models.CharField(max_length=255)
    sluggable_id = models.IntegerField()
    sluggable_type = models.CharField(max_length=50, blank=True, null=True)
    scope = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendly_id_slugs'
        unique_together = (('slug', 'sluggable_type', 'scope'),)
