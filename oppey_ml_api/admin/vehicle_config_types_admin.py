from django.contrib import admin
from oppey_ml_api.models import VehicleConfigTypes


@admin.register(VehicleConfigTypes)
class VehicleConfigTypesAdmin(admin.ModelAdmin):
    pass
