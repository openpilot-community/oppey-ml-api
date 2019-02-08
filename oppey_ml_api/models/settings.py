from django.db import models


class Settings(models.Model):
    botid = models.CharField(db_column='botID', primary_key=True, max_length=255)  # Field name made lowercase.
    relaydirectmessages = models.BooleanField(db_column='relayDirectMessages')  # Field name made lowercase.
    blacklistedguilds = models.TextField(db_column='blacklistedGuilds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blacklistedusers = models.TextField(db_column='blacklistedUsers', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settings'
