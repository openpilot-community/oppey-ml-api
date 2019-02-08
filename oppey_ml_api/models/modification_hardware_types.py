from django.db import models


class ModificationHardwareTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    modification = models.ForeignKey('Modifications', models.DO_NOTHING, blank=True, null=True)
    hardware_type = models.ForeignKey('HardwareTypes', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modification_hardware_types'
