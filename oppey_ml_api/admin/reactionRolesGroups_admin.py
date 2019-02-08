from django.contrib import admin
from oppey_ml_api.models import Reactionrolesgroups


@admin.register(Reactionrolesgroups)
class ReactionrolesgroupsAdmin(admin.ModelAdmin):
    pass
