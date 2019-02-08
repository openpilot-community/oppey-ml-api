from django.db import models


class DjangoChatterbotStatementTags(models.Model):
    statement = models.ForeignKey('DjangoChatterbotStatement', models.DO_NOTHING)
    tag = models.ForeignKey('DjangoChatterbotTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_chatterbot_statement_tags'
        unique_together = (('statement', 'tag'),)
