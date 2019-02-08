from django.contrib import admin
from oppey_ml_api.models import VehicleConfigTrims


@admin.register(VehicleConfigTrims)
class VehicleConfigTrimsAdmin(admin.ModelAdmin):
    pass
