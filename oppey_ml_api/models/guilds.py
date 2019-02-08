from django.db import models


class Guilds(models.Model):
    guildid = models.CharField(db_column='guildID', primary_key=True, max_length=255)  # Field name made lowercase.
    enabled = models.BooleanField()
    premium = models.BooleanField()
    description = models.BinaryField(blank=True, null=True)
    icon = models.CharField(max_length=2048, blank=True, null=True)
    prefix = models.TextField()  # This field type is a guess.
    language = models.CharField(max_length=255, blank=True, null=True)
    greet = models.CharField(max_length=255, blank=True, null=True)
    greetmessage = models.TextField(db_column='greetMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    greettimeout = models.IntegerField(db_column='greetTimeout')  # Field name made lowercase.
    greetprivate = models.BooleanField(db_column='greetPrivate')  # Field name made lowercase.
    greetprivatemessage = models.TextField(db_column='greetPrivateMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    farewell = models.CharField(max_length=255, blank=True, null=True)
    farewellmessage = models.TextField(db_column='farewellMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    farewelltimeout = models.IntegerField(db_column='farewellTimeout')  # Field name made lowercase.
    music = models.BooleanField()
    chat = models.BooleanField()
    levelups = models.BooleanField(db_column='levelUps')  # Field name made lowercase.
    levelupmessages = models.BooleanField(db_column='levelUpMessages')  # Field name made lowercase.
    musicautoplay = models.BooleanField(db_column='musicAutoPlay')  # Field name made lowercase.
    musicautodisconnect = models.BooleanField(db_column='musicAutoDisconnect')  # Field name made lowercase.
    musictextchannel = models.CharField(db_column='musicTextChannel', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    musicvoicechannel = models.CharField(db_column='musicVoiceChannel', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    musicmasterrole = models.CharField(db_column='musicMasterRole', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    autoassignableroles = models.TextField(db_column='autoAssignableRoles', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selfassignableroles = models.TextField(db_column='selfAssignableRoles', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    streamerrole = models.CharField(db_column='streamerRole', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    uncoversneakylinks = models.BooleanField(db_column='uncoverSneakyLinks')  # Field name made lowercase.
    filteremojis = models.BooleanField(db_column='filterEmojis')  # Field name made lowercase.
    filterinvites = models.BooleanField(db_column='filterInvites')  # Field name made lowercase.
    filterlinks = models.BooleanField(db_column='filterLinks')  # Field name made lowercase.
    filtermentions = models.BooleanField(db_column='filterMentions')  # Field name made lowercase.
    filterwords = models.BooleanField(db_column='filterWords')  # Field name made lowercase.
    filteredwords = models.TextField(db_column='filteredWords', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    whitelisteddomains = models.TextField(db_column='whitelistedDomains', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    whitelistedinvites = models.TextField(db_column='whitelistedInvites', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mentionspamthreshold = models.IntegerField(db_column='mentionSpamThreshold', blank=True, null=True)  # Field name made lowercase.
    mentionspamaction = models.CharField(db_column='mentionSpamAction', max_length=255, blank=True, null=True)  # Field name made lowercase.
    warnthreshold = models.IntegerField(db_column='warnThreshold')  # Field name made lowercase.
    warnaction = models.CharField(db_column='warnAction', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serverlog = models.CharField(db_column='serverLog', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    moderationlog = models.CharField(db_column='moderationLog', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    moderationcaseno = models.CharField(db_column='moderationCaseNo', max_length=255)  # Field name made lowercase.
    starboard = models.CharField(unique=True, max_length=255, blank=True, null=True)
    announcementchannel = models.CharField(db_column='announcementChannel', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    reportchannel = models.CharField(db_column='reportChannel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suggestionchannel = models.CharField(db_column='suggestionChannel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wordofthedaychannel = models.CharField(db_column='wordOfTheDayChannel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    botrole = models.CharField(db_column='botRole', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disabledcommands = models.TextField(db_column='disabledCommands', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    allowedroles = models.TextField(db_column='allowedRoles', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    allowedchannels = models.TextField(db_column='allowedChannels', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    membersonly = models.BooleanField(db_column='membersOnly')  # Field name made lowercase.
    antiraid = models.IntegerField(db_column='antiRaid')  # Field name made lowercase.
    autodeletecommandoutput = models.BooleanField(db_column='autoDeleteCommandOutput')  # Field name made lowercase.
    gambling = models.BooleanField()
    showpermserror = models.BooleanField(db_column='showPermsError')  # Field name made lowercase.
    celebratebirthday = models.BooleanField(db_column='celebrateBirthday')  # Field name made lowercase.
    reactionannouncements = models.BooleanField(db_column='reactionAnnouncements')  # Field name made lowercase.
    reactionpinning = models.BooleanField(db_column='reactionPinning')  # Field name made lowercase.
    carepackages = models.BooleanField(db_column='carePackages')  # Field name made lowercase.
    commonmisspellingchecker = models.BooleanField(db_column='commonMisspellingChecker')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guilds'
