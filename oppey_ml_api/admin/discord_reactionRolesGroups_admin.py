from django.contrib import admin
from oppey_ml_api.models import DiscordReactionrolesgroups


@admin.register(DiscordReactionrolesgroups)
class DiscordReactionrolesgroupsAdmin(admin.ModelAdmin):
    pass
