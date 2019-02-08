from django.contrib import admin
from oppey_ml_api.models import HardwareItems


@admin.register(HardwareItems)
class HardwareItemsAdmin(admin.ModelAdmin):
    pass
