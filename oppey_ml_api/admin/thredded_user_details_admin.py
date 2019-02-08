from django.contrib import admin
from oppey_ml_api.models import ThreddedUserDetails


@admin.register(ThreddedUserDetails)
class ThreddedUserDetailsAdmin(admin.ModelAdmin):
    pass
