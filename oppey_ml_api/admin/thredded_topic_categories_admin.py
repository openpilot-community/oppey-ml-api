from django.contrib import admin
from oppey_ml_api.models import ThreddedTopicCategories


@admin.register(ThreddedTopicCategories)
class ThreddedTopicCategoriesAdmin(admin.ModelAdmin):
    pass
