from django.contrib import admin
from oppey_ml_api.models import ThreddedPrivateUsers


@admin.register(ThreddedPrivateUsers)
class ThreddedPrivateUsersAdmin(admin.ModelAdmin):
    pass
