from django.contrib import admin
from oppey_ml_api.models import ShortenedUrls


@admin.register(ShortenedUrls)
class ShortenedUrlsAdmin(admin.ModelAdmin):
    pass
