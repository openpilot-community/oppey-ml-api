from django.contrib import admin
from oppey_ml_api.models import VehicleTrims


@admin.register(VehicleTrims)
class VehicleTrimsAdmin(admin.ModelAdmin):
    pass
