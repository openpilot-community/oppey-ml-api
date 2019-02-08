from django.db import models


class GuideHardwareItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    guide = models.ForeignKey('Guides', models.DO_NOTHING, blank=True, null=True)
    hardware_item = models.ForeignKey('HardwareItems', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'guide_hardware_items'
