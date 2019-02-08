from django.contrib import admin
from oppey_ml_api.models import VehicleModels


@admin.register(VehicleModels)
class VehicleModelsAdmin(admin.ModelAdmin):
    pass
