from django.contrib import admin
from oppey_ml_api.models import VehicleConfigImages


@admin.register(VehicleConfigImages)
class VehicleConfigImagesAdmin(admin.ModelAdmin):
    pass
