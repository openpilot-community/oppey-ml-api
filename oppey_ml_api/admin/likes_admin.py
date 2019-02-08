from django.contrib import admin
from oppey_ml_api.models import Likes


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass
