from django.contrib import admin
from oppey_ml_api.models import ModificationHardwareTypeHardwareItems


@admin.register(ModificationHardwareTypeHardwareItems)
class ModificationHardwareTypeHardwareItemsAdmin(admin.ModelAdmin):
    pass
