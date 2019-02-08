from django.contrib import admin
from oppey_ml_api.models import ThreddedTopics


@admin.register(ThreddedTopics)
class ThreddedTopicsAdmin(admin.ModelAdmin):
    pass
