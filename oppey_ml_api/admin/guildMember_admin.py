from django.contrib import admin
from oppey_ml_api.models import Guildmember


@admin.register(Guildmember)
class GuildmemberAdmin(admin.ModelAdmin):
    pass
