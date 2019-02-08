from django.contrib import admin
from oppey_ml_api.models import ThreddedCategories


@admin.register(ThreddedCategories)
class ThreddedCategoriesAdmin(admin.ModelAdmin):
    pass
