from django.db import models


class DiscordUserVehicles(models.Model):
    discord_user = models.ForeignKey('DiscordUsers', models.DO_NOTHING, blank=True, null=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    vehicle_year = models.IntegerField(blank=True, null=True)
    vehicle_make = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_trim = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discord_user_vehicles'
