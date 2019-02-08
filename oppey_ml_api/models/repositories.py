from django.db import models


class Repositories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    owner_login = models.CharField(max_length=255, blank=True, null=True)
    owner_avatar_url = models.CharField(max_length=255, blank=True, null=True)
    owner_url = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'repositories'
