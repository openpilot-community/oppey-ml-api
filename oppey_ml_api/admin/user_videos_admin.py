from django.contrib import admin
from oppey_ml_api.models import UserVideos


@admin.register(UserVideos)
class UserVideosAdmin(admin.ModelAdmin):
    pass
