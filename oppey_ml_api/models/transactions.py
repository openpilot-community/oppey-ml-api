from django.db import models


class Transactions(models.Model):
    userid = models.CharField(db_column='userID', max_length=255)  # Field name made lowercase.
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    type = models.CharField(max_length=255)
    amount = models.TextField()
    note = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactions'
