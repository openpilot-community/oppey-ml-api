from django.db import models


class DiscordModerationcases(models.Model):
    guildid = models.CharField(db_column='guildID', max_length=255)  # Field name made lowercase.
    number = models.CharField(max_length=255)
    messageid = models.CharField(db_column='messageID', unique=True, max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discord_moderationCases'
