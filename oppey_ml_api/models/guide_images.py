from django.db import models


class GuideImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    guide_id = models.BigIntegerField(blank=True, null=True)
    image_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'guide_images'
