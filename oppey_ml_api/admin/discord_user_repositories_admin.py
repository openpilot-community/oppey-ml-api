from django.contrib import admin
from oppey_ml_api.models import DiscordUserRepositories


@admin.register(DiscordUserRepositories)
class DiscordUserRepositoriesAdmin(admin.ModelAdmin):
    pass
