from django.db import models


class ScheduledCommands(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    channelid = models.CharField(db_column='channelID', max_length=255)  # Field name made lowercase.
    messageid = models.CharField(db_column='messageID', max_length=255)  # Field name made lowercase.
    cronexp = models.CharField(db_column='cronExp', max_length=255)  # Field name made lowercase.
    command = models.CharField(max_length=255)
    arguments = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scheduled_commands'
