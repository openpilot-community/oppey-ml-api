from django.contrib import admin
from oppey_ml_api.models import VehicleConfigCapabilities


@admin.register(VehicleConfigCapabilities)
class VehicleConfigCapabilitiesAdmin(admin.ModelAdmin):
    pass
