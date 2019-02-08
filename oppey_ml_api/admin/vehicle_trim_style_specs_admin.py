from django.contrib import admin
from oppey_ml_api.models import VehicleTrimStyleSpecs


@admin.register(VehicleTrimStyleSpecs)
class VehicleTrimStyleSpecsAdmin(admin.ModelAdmin):
    pass
