from django.db import models


class Streamers(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID', primary_key=True)  # Field name made lowercase.
    channelid = models.CharField(db_column='channelID', unique=True, max_length=255)  # Field name made lowercase.
    message = models.BinaryField(blank=True, null=True)
    mixer = models.TextField(blank=True, null=True)  # This field type is a guess.
    twitch = models.TextField(blank=True, null=True)  # This field type is a guess.
    youtube = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'streamers'
