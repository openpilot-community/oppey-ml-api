from django.db import models


class GuildMembers(models.Model):
    userid = models.CharField(db_column='userID', max_length=255)  # Field name made lowercase.
    guildid = models.CharField(db_column='guildID', max_length=255)  # Field name made lowercase.
    bastioncurrencies = models.TextField(db_column='bastionCurrencies')  # Field name made lowercase.
    experiencepoints = models.TextField(db_column='experiencePoints')  # Field name made lowercase.
    level = models.TextField()
    karma = models.TextField()
    blacklisted = models.BooleanField()
    lastclaimed = models.DateTimeField(db_column='lastClaimed', blank=True, null=True)  # Field name made lowercase.
    claimstreak = models.IntegerField(db_column='claimStreak', blank=True, null=True)  # Field name made lowercase.
    warnings = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guild_members'
        unique_together = (('userid', 'guildid'),)
