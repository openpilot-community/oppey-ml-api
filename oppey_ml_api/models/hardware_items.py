from django.db import models


class HardwareItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    alternate_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hardware_type = models.ForeignKey('HardwareTypes', models.DO_NOTHING, blank=True, null=True)
    compatible_with_all_vehicles = models.NullBooleanField()
    available_for_purchase = models.NullBooleanField()
    purchase_url = models.CharField(max_length=255, blank=True, null=True)
    requires_assembly = models.NullBooleanField()
    can_be_built = models.NullBooleanField()
    build_plans_url = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    install_guide_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    source_image_url = models.CharField(max_length=255, blank=True, null=True)
    description_markup = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware_items'
