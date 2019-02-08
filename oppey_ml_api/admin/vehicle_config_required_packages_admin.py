from django.contrib import admin
from oppey_ml_api.models import VehicleConfigRequiredPackages


@admin.register(VehicleConfigRequiredPackages)
class VehicleConfigRequiredPackagesAdmin(admin.ModelAdmin):
    pass
