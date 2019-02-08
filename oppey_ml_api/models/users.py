from django.db import models


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    slack_username = models.CharField(max_length=255, blank=True, null=True)
    github_username = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.ForeignKey('UserRoles', models.DO_NOTHING, blank=True, null=True)
    guest = models.NullBooleanField()
    discord_username = models.CharField(max_length=255, blank=True, null=True)
    openpilot_experience = models.CharField(max_length=255, blank=True, null=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    youtube_channel_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_username = models.CharField(max_length=255, blank=True, null=True)
    bio_markdown = models.TextField(blank=True, null=True)
    bio_markup = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
