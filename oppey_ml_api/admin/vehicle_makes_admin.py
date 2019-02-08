from django.contrib import admin
from oppey_ml_api.models import VehicleMakes


@admin.register(VehicleMakes)
class VehicleMakesAdmin(admin.ModelAdmin):
    pass
