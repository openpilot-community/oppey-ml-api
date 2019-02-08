from django.db import models


class Versions(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_type = models.CharField(max_length=255)
    item_id = models.IntegerField()
    event = models.CharField(max_length=255)
    whodunnit = models.CharField(max_length=255, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    object_changes = models.TextField(blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'
