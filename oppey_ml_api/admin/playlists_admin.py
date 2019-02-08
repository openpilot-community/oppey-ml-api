from django.contrib import admin
from oppey_ml_api.models import Playlists


@admin.register(Playlists)
class PlaylistsAdmin(admin.ModelAdmin):
    pass
