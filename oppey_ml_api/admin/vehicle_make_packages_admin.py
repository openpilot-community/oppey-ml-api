from django.contrib import admin
from oppey_ml_api.models import VehicleMakePackages


@admin.register(VehicleMakePackages)
class VehicleMakePackagesAdmin(admin.ModelAdmin):
    pass
