from django.contrib import admin
from oppey_ml_api.models import Shops


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    pass
