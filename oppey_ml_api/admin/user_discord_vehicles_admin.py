from django.contrib import admin
from oppey_ml_api.models import UserDiscordVehicles


@admin.register(UserDiscordVehicles)
class UserDiscordVehiclesAdmin(admin.ModelAdmin):
    pass
