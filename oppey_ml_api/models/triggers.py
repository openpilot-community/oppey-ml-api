from django.db import models


class Triggers(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    trigger = models.TextField()
    responsemessage = models.TextField(db_column='responseMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    responsereactions = models.TextField(db_column='responseReactions', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'triggers'
