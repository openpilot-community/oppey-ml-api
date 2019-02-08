from django.contrib import admin
from oppey_ml_api.models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass
