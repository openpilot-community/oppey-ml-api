from django.contrib import admin
from oppey_ml_api.models import DiscordModerationcases


@admin.register(DiscordModerationcases)
class DiscordModerationcasesAdmin(admin.ModelAdmin):
    pass
