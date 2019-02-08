from django.db import models


class DiscordMessages(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    discord_channel_id = models.CharField(max_length=255)
    discord_user = models.ForeignKey('DiscordUsers', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    attachment_ids = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    jump_url = models.CharField(max_length=255, blank=True, null=True)
    trained = models.BooleanField(blank=False,null=False,default=False)

    class Meta:
        managed = False
        db_table = 'discord_messages'
