from django.contrib import admin
from oppey_ml_api.models import CabanaLinks


@admin.register(CabanaLinks)
class CabanaLinksAdmin(admin.ModelAdmin):
    pass
