from django.db import models


class DiscordReactionrolesgroups(models.Model):
    messageid = models.CharField(db_column='messageID', max_length=255)  # Field name made lowercase.
    channelid = models.CharField(db_column='channelID', max_length=255)  # Field name made lowercase.
    guildid = models.CharField(db_column='guildID', max_length=255)  # Field name made lowercase.
    reactionroles = models.TextField(db_column='reactionRoles', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mutuallyexclusive = models.BooleanField(db_column='mutuallyExclusive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discord_reactionRolesGroups'
