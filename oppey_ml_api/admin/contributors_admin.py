from django.contrib import admin
from oppey_ml_api.models import Contributors


@admin.register(Contributors)
class ContributorsAdmin(admin.ModelAdmin):
    pass
