from django.contrib import admin
from oppey_ml_api.models import ScheduledCommands


@admin.register(ScheduledCommands)
class ScheduledCommandsAdmin(admin.ModelAdmin):
    pass
