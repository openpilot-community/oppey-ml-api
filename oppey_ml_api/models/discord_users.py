from django.db import models


class DiscordUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    afk = models.BooleanField()
    afkmessage = models.CharField(max_length=255, blank=True, null=True)
    blacklisted = models.NullBooleanField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    last_seen_at = models.DateTimeField(blank=True, null=True)
    last_seen_in = models.CharField(max_length=255, blank=True, null=True)
    total_messages = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discord_users'
