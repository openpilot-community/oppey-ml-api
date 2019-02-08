from django.contrib import admin
from oppey_ml_api.models import ThreddedPosts


@admin.register(ThreddedPosts)
class ThreddedPostsAdmin(admin.ModelAdmin):
    pass
