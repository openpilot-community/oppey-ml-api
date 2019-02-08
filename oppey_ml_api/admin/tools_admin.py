from django.contrib import admin
from oppey_ml_api.models import Tools


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    pass
