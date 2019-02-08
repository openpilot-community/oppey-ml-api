from django.contrib import admin
from oppey_ml_api.models import Follows


@admin.register(Follows)
class FollowsAdmin(admin.ModelAdmin):
    pass
