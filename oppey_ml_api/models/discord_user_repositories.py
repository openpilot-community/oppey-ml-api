from django.db import models


class DiscordUserRepositories(models.Model):
    discord_user = models.ForeignKey('DiscordUsers', models.DO_NOTHING, blank=True, null=True)
    repository = models.ForeignKey('Repositories', models.DO_NOTHING, blank=True, null=True)
    repository_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discord_user_repositories'
