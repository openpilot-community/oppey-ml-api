from django.db import models


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
