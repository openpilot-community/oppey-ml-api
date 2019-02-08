from django.contrib import admin
from oppey_ml_api.models import VehicleOptionAvailabilities


@admin.register(VehicleOptionAvailabilities)
class VehicleOptionAvailabilitiesAdmin(admin.ModelAdmin):
    pass
