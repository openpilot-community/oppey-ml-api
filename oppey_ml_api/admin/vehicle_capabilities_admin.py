from django.contrib import admin
from oppey_ml_api.models import VehicleCapabilities


@admin.register(VehicleCapabilities)
class VehicleCapabilitiesAdmin(admin.ModelAdmin):
    pass
