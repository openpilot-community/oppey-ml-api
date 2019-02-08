from django.contrib import admin
from oppey_ml_api.models import VehicleConfigModifications


@admin.register(VehicleConfigModifications)
class VehicleConfigModificationsAdmin(admin.ModelAdmin):
    pass
