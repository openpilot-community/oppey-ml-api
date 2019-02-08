from django.db import models


class OpenrecordMigrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openrecord_migrations'
