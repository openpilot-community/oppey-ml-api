from django.contrib import admin
from oppey_ml_api.models import VehicleTrimStyles


@admin.register(VehicleTrimStyles)
class VehicleTrimStylesAdmin(admin.ModelAdmin):
    pass
