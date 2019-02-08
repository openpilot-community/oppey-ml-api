from django.db import models


class Playlists(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    songs = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlists'
