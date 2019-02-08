from django.contrib import admin
from oppey_ml_api.models import ModificationHardwareTypes


@admin.register(ModificationHardwareTypes)
class ModificationHardwareTypesAdmin(admin.ModelAdmin):
    pass
