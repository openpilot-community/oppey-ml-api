from django.contrib import admin
from oppey_ml_api.models import PullRequests


@admin.register(PullRequests)
class PullRequestsAdmin(admin.ModelAdmin):
    pass
