from django.contrib import admin
from oppey_ml_api.models import DiscordScheduledcommands


@admin.register(DiscordScheduledcommands)
class DiscordScheduledcommandsAdmin(admin.ModelAdmin):
    pass
