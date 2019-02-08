from django.contrib import admin
from oppey_ml_api.models import VehicleConfigs


@admin.register(VehicleConfigs)
class VehicleConfigsAdmin(admin.ModelAdmin):
    pass
