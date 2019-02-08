from django.contrib import admin
from oppey_ml_api.models import DiscordUsers


@admin.register(DiscordUsers)
class DiscordUsersAdmin(admin.ModelAdmin):
    pass
