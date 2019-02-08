from django.contrib import admin
from oppey_ml_api.models import Videos


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    pass
