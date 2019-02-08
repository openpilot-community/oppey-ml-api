from django.db import models


class ModerationCases(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    number = models.CharField(max_length=255)
    messageid = models.CharField(db_column='messageID', unique=True, max_length=255)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'moderation_cases'
