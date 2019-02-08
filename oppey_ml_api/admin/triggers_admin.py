from django.contrib import admin
from oppey_ml_api.models import Triggers


@admin.register(Triggers)
class TriggersAdmin(admin.ModelAdmin):
    pass
