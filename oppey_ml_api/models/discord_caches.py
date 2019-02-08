from django.db import models


class DiscordCaches(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discord_caches'
