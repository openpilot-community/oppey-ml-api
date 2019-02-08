from django.db import models


class TextChannels(models.Model):
    channelid = models.CharField(db_column='channelID', primary_key=True, max_length=255)  # Field name made lowercase.
    guildid = models.ForeignKey('Guilds', models.DO_NOTHING, db_column='guildID')  # Field name made lowercase.
    language = models.CharField(max_length=255, blank=True, null=True)
    fileonly = models.BooleanField(db_column='fileOnly')  # Field name made lowercase.
    videoonly = models.BooleanField(db_column='videoOnly')  # Field name made lowercase.
    imageonly = models.BooleanField(db_column='imageOnly')  # Field name made lowercase.
    soundonly = models.BooleanField(db_column='soundOnly')  # Field name made lowercase.
    votingchannel = models.BooleanField(db_column='votingChannel')  # Field name made lowercase.
    ignoreemojifilter = models.BooleanField(db_column='ignoreEmojiFilter')  # Field name made lowercase.
    ignoreinvitefilter = models.BooleanField(db_column='ignoreInviteFilter')  # Field name made lowercase.
    ignorelinkfilter = models.BooleanField(db_column='ignoreLinkFilter')  # Field name made lowercase.
    ignorementionfilter = models.BooleanField(db_column='ignoreMentionFilter')  # Field name made lowercase.
    ignorewordfilter = models.BooleanField(db_column='ignoreWordFilter')  # Field name made lowercase.
    ignorestarboard = models.BooleanField(db_column='ignoreStarboard')  # Field name made lowercase.
    ignorexp = models.BooleanField(db_column='ignoreXP')  # Field name made lowercase.
    disabledcommands = models.TextField(db_column='disabledCommands', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blacklisted = models.BooleanField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'text_channels'
        unique_together = (('channelid', 'guildid'),)
