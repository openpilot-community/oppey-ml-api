from django.contrib import admin
from oppey_ml_api.models import Scheduledcommands


@admin.register(Scheduledcommands)
class ScheduledcommandsAdmin(admin.ModelAdmin):
    pass
