from django.contrib import admin
from oppey_ml_api.models import ThreddedPrivatePosts


@admin.register(ThreddedPrivatePosts)
class ThreddedPrivatePostsAdmin(admin.ModelAdmin):
    pass
