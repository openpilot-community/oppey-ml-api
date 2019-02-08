from django.db import models


class ModificationHardwareItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    modification = models.ForeignKey('Modifications', models.DO_NOTHING, blank=True, null=True)
    hardware_item = models.ForeignKey('HardwareItems', models.DO_NOTHING, blank=True, null=True)
    used_for = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modification_hardware_items'
