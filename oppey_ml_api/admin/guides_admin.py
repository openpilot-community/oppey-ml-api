from django.contrib import admin
from oppey_ml_api.models import Guides


@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    pass
