from django.db import models


class VersionAssociations(models.Model):
    id = models.BigAutoField(primary_key=True)
    version_id = models.IntegerField(blank=True, null=True)
    foreign_key_name = models.CharField(max_length=255)
    foreign_key_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_associations'
