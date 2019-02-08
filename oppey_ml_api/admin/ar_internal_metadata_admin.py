from django.contrib import admin
from oppey_ml_api.models import ArInternalMetadata


@admin.register(ArInternalMetadata)
class ArInternalMetadataAdmin(admin.ModelAdmin):
    pass
