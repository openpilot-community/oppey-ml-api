from django.contrib import admin
from oppey_ml_api.models import VehicleSpecs


@admin.register(VehicleSpecs)
class VehicleSpecsAdmin(admin.ModelAdmin):
    pass
