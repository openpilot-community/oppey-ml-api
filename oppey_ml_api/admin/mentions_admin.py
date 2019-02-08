from django.contrib import admin
from oppey_ml_api.models import Mentions


@admin.register(Mentions)
class MentionsAdmin(admin.ModelAdmin):
    pass
