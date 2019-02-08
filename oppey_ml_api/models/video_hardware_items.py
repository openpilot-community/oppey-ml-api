from django.db import models


class VideoHardwareItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)
    hardware_item = models.ForeignKey('HardwareItems', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'video_hardware_items'
