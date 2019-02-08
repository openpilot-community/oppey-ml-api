from django.contrib import admin
from oppey_ml_api.models import GuildMembers


@admin.register(GuildMembers)
class GuildMembersAdmin(admin.ModelAdmin):
    pass
