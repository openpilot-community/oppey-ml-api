from django.contrib import admin
from oppey_ml_api.models import VehicleConfigHardwareItems


@admin.register(VehicleConfigHardwareItems)
class VehicleConfigHardwareItemsAdmin(admin.ModelAdmin):
    pass
