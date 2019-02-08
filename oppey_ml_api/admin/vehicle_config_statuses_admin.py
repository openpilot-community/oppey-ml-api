from django.contrib import admin
from oppey_ml_api.models import VehicleConfigStatuses


@admin.register(VehicleConfigStatuses)
class VehicleConfigStatusesAdmin(admin.ModelAdmin):
    pass
