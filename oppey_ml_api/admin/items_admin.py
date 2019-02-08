from django.contrib import admin
from oppey_ml_api.models import Items


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass
