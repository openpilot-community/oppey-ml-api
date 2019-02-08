from django.contrib import admin
from oppey_ml_api.models import DiscordSettings


@admin.register(DiscordSettings)
class DiscordSettingsAdmin(admin.ModelAdmin):
    pass
