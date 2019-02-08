from django.contrib import admin
from oppey_ml_api.models import GuideImages


@admin.register(GuideImages)
class GuideImagesAdmin(admin.ModelAdmin):
    pass
