from django.contrib import admin
from oppey_ml_api.models import Guildmembers


@admin.register(Guildmembers)
class GuildmembersAdmin(admin.ModelAdmin):
    pass
