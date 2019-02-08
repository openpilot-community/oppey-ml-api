from django.contrib import admin
from oppey_ml_api.models import UserVehicles


@admin.register(UserVehicles)
class UserVehiclesAdmin(admin.ModelAdmin):
    pass
