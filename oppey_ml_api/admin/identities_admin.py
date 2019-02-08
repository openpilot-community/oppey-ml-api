from django.contrib import admin
from oppey_ml_api.models import Identities


@admin.register(Identities)
class IdentitiesAdmin(admin.ModelAdmin):
    pass
