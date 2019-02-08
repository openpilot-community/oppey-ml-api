from django.contrib import admin
from oppey_ml_api.models import DiscordUserVehicles


@admin.register(DiscordUserVehicles)
class DiscordUserVehiclesAdmin(admin.ModelAdmin):
    pass
