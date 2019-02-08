from django.contrib import admin
from oppey_ml_api.models import VehicleLookups


@admin.register(VehicleLookups)
class VehicleLookupsAdmin(admin.ModelAdmin):
    pass
