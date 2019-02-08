from django.db import models


class ReleaseFeatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    release = models.ForeignKey('Releases', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'release_features'
