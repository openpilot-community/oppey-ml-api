from django.contrib import admin
from oppey_ml_api.models import DiscordMessages


@admin.register(DiscordMessages)
class DiscordMessagesAdmin(admin.ModelAdmin):
    pass
