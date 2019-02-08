from django.contrib import admin
from oppey_ml_api.models import DiscordCaches


@admin.register(DiscordCaches)
class DiscordCachesAdmin(admin.ModelAdmin):
    pass
