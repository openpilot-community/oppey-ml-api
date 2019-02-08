from django.db import models


class ModificationHardwareTypeHardwareItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    modification_hardware_type = models.ForeignKey('ModificationHardwareTypes', models.DO_NOTHING, blank=True, null=True)
    hardware_item = models.ForeignKey('HardwareItems', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modification_hardware_type_hardware_items'
