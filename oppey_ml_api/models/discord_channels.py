from django.db import models
from django.contrib.postgres.fields import JSONField


class DiscordChannels(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    parent_id = models.CharField(max_length=255)
    discord_guild_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    topic = models.CharField(max_length=1000)
    discord_last_message_id = models.CharField(max_length=255)
    raw_position = models.IntegerField(blank=False,null=False,default=0)
    rate_limit_per_user = models.IntegerField(blank=False,null=False,default=0)
    deleted = models.BooleanField(blank=False,null=False,default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discord_channels'
