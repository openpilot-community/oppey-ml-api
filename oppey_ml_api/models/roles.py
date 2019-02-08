from django.db import models


class Roles(models.Model):
    roleid = models.CharField(db_column='roleID', primary_key=True, max_length=255)  # Field name made lowercase.
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    description = models.BinaryField(blank=True, null=True)
    icon = models.CharField(max_length=2048, blank=True, null=True)
    ignoreemojifilter = models.BooleanField(db_column='ignoreEmojiFilter')  # Field name made lowercase.
    ignoreinvitefilter = models.BooleanField(db_column='ignoreInviteFilter')  # Field name made lowercase.
    ignorelinkfilter = models.BooleanField(db_column='ignoreLinkFilter')  # Field name made lowercase.
    ignorementionfilter = models.BooleanField(db_column='ignoreMentionFilter')  # Field name made lowercase.
    ignorewordfilter = models.BooleanField(db_column='ignoreWordFilter')  # Field name made lowercase.
    ignorestarboard = models.BooleanField(db_column='ignoreStarboard')  # Field name made lowercase.
    ignorexp = models.BooleanField(db_column='ignoreXP')  # Field name made lowercase.
    disabledcommands = models.TextField(db_column='disabledCommands', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    level = models.CharField(max_length=255, blank=True, null=True)
    exclusive = models.BooleanField()
    price = models.TextField(blank=True, null=True)
    emoji = models.CharField(max_length=255, blank=True, null=True)
    blacklisted = models.BooleanField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'
        unique_together = (('roleid', 'guildid'),)
