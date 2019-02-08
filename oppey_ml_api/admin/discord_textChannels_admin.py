from django.contrib import admin
from oppey_ml_api.models import DiscordTextchannels


@admin.register(DiscordTextchannels)
class DiscordTextchannelsAdmin(admin.ModelAdmin):
    pass
