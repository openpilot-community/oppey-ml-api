from django.contrib import admin
from oppey_ml_api.models import UntitledTable


@admin.register(UntitledTable)
class UntitledTableAdmin(admin.ModelAdmin):
    pass
