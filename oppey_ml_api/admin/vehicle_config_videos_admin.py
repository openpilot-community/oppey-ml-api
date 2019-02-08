from django.contrib import admin
from oppey_ml_api.models import VehicleConfigVideos


@admin.register(VehicleConfigVideos)
class VehicleConfigVideosAdmin(admin.ModelAdmin):
    pass
