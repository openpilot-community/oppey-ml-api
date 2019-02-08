from django.contrib import admin
from oppey_ml_api.models import VehicleConfigGuides


@admin.register(VehicleConfigGuides)
class VehicleConfigGuidesAdmin(admin.ModelAdmin):
    pass
