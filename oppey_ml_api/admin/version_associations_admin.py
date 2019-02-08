from django.contrib import admin
from oppey_ml_api.models import VersionAssociations


@admin.register(VersionAssociations)
class VersionAssociationsAdmin(admin.ModelAdmin):
    pass
