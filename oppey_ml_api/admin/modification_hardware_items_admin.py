from django.contrib import admin
from oppey_ml_api.models import ModificationHardwareItems


@admin.register(ModificationHardwareItems)
class ModificationHardwareItemsAdmin(admin.ModelAdmin):
    pass
