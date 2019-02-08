from django.contrib import admin
from oppey_ml_api.models import ReactionRolesGroups


@admin.register(ReactionRolesGroups)
class ReactionRolesGroupsAdmin(admin.ModelAdmin):
    pass
