from django.contrib import admin
from oppey_ml_api.models import VehicleOptions


@admin.register(VehicleOptions)
class VehicleOptionsAdmin(admin.ModelAdmin):
    pass
