from django.contrib import admin
from oppey_ml_api.models import VehicleModelOptions


@admin.register(VehicleModelOptions)
class VehicleModelOptionsAdmin(admin.ModelAdmin):
    pass
