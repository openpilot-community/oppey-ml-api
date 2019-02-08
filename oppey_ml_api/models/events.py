from django.db import models


class Events(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.BinaryField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'
