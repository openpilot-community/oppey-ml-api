from django.contrib import admin
from oppey_ml_api.models import VehicleConfigRequiredOptions


@admin.register(VehicleConfigRequiredOptions)
class VehicleConfigRequiredOptionsAdmin(admin.ModelAdmin):
    pass
