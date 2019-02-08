from django.contrib import admin
from oppey_ml_api.models import ThreddedUserTopicFollows


@admin.register(ThreddedUserTopicFollows)
class ThreddedUserTopicFollowsAdmin(admin.ModelAdmin):
    pass
