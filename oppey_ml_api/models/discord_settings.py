from django.db import models


class DiscordSettings(models.Model):
    guild = models.CharField(primary_key=True, max_length=255)
    settings = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'discord_settings'
