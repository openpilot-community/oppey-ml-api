from django.db import models


class DjangoChatterbotTag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'django_chatterbot_tag'
