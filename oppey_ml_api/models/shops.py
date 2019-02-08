from django.db import models


class Shops(models.Model):
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID', primary_key=True)  # Field name made lowercase.
    custom = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shops'
