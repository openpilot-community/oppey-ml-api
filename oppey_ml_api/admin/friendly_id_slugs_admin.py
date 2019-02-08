from django.contrib import admin
from oppey_ml_api.models import FriendlyIdSlugs


@admin.register(FriendlyIdSlugs)
class FriendlyIdSlugsAdmin(admin.ModelAdmin):
    pass
