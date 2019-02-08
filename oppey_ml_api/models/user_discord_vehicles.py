from django.db import models


class UserDiscordVehicles(models.Model):
    id = models.BigAutoField(primary_key=True)
    discord_user_id = models.CharField(max_length=255, blank=True, null=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_discord_vehicles'
